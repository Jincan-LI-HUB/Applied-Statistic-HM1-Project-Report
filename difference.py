import pandas as pd
import numpy as np

def compare_csv_files(clean_file_path, raw_file_path):
    """
    比较两个CSV文件的异同
    """
    print("="*60)
    print("CSV文件差异比较分析")
    print("="*60)
    
    # 读取两个文件
    try:
        df_clean = pd.read_csv(clean_file_path)
        df_raw = pd.read_csv(raw_file_path)
        print(f"✓ 成功读取文件:")
        print(f"  - 清洗文件: {clean_file_path}")
        print(f"  - 原始文件: {raw_file_path}")
    except FileNotFoundError as e:
        print(f"✗ 文件未找到: {e}")
        return
    except Exception as e:
        print(f"✗ 读取文件时出错: {e}")
        return

    print("\n" + "="*40)
    print("基础信息对比")
    print("="*40)
    
    # 基础信息
    print(f"清洗文件形状: {df_clean.shape}")
    print(f"原始文件形状: {df_raw.shape}")
    
    rows_clean, cols_clean = df_clean.shape
    rows_raw, cols_raw = df_raw.shape
    
    print(f"\n行数差异: 清洗文件比原始文件 {'多' if rows_clean > rows_raw else '少'} {abs(rows_clean - rows_raw)} 行")
    print(f"列数差异: 清洗文件比原始文件 {'多' if cols_clean > cols_raw else '少'} {abs(cols_clean - cols_raw)} 列")

    print("\n" + "="*40)
    print("列名对比")
    print("="*40)
    
    clean_cols = set(df_clean.columns)
    raw_cols = set(df_raw.columns)
    
    print(f"清洗文件列数: {len(clean_cols)}")
    print(f"原始文件列数: {len(raw_cols)}")
    
    only_in_clean = clean_cols - raw_cols
    only_in_raw = raw_cols - clean_cols
    common_cols = clean_cols & raw_cols
    
    if only_in_clean:
        print(f"\n仅存在于清洗文件的列 ({len(only_in_clean)}):")
        for col in sorted(only_in_clean):
            print(f"  - {col}")
    
    if only_in_raw:
        print(f"\n仅存在于原始文件的列 ({len(only_in_raw)}):")
        for col in sorted(only_in_raw):
            print(f"  - {col}")
    
    print(f"\n共同列数: {len(common_cols)}")
    
    print("\n" + "="*40)
    print("数据类型对比")
    print("="*40)
    
    # 数据类型对比
    type_diffs = []
    for col in common_cols:
        clean_dtype = str(df_clean[col].dtype)
        raw_dtype = str(df_raw[col].dtype)
        if clean_dtype != raw_dtype:
            type_diffs.append((col, clean_dtype, raw_dtype))
    
    if type_diffs:
        print("数据类型不同的列:")
        for col, clean_dtype, raw_dtype in type_diffs:
            print(f"  - {col}: 清洗文件({clean_dtype}) vs 原始文件({raw_dtype})")
    else:
        print("✓ 所有共同列的数据类型相同")
    
    print("\n" + "="*40)
    print("数值统计对比")
    print("="*40)
    
    # 数值列的统计信息对比
    numeric_cols_clean = df_clean.select_dtypes(include=[np.number]).columns
    numeric_cols_raw = df_raw.select_dtypes(include=[np.number]).columns
    
    common_numeric = set(numeric_cols_clean) & set(numeric_cols_raw)
    
    if common_numeric:
        print("共同数值列的基本统计信息对比:")
        for col in sorted(common_numeric):
            print(f"\n列 '{col}' 统计信息:")
            print("  清洗文件:")
            print(f"    计数: {df_clean[col].count()}, 平均值: {df_clean[col].mean():.2f}, 标准差: {df_clean[col].std():.2f}")
            print("  原始文件:")
            print(f"    计数: {df_raw[col].count()}, 平均值: {df_raw[col].mean():.2f}, 标准差: {df_raw[col].std():.2f}")
            
            # 检查数值是否有显著差异
            clean_mean = df_clean[col].mean()
            raw_mean = df_raw[col].mean()
            if not pd.isna(clean_mean) and not pd.isna(raw_mean):
                diff_ratio = abs(clean_mean - raw_mean) / max(abs(raw_mean), 1e-8)
                if diff_ratio > 0.01:  # 差异超过1%
                    print(f"    ⚠️  平均值差异较大: {diff_ratio:.2%}")
    else:
        print("⚠️  无共同数值列")
    
    print("\n" + "="*40)
    print("缺失值对比")
    print("="*40)
    
    # 缺失值对比
    missing_clean = df_clean.isnull().sum()
    missing_raw = df_raw.isnull().sum()
    
    missing_comparison = pd.DataFrame({
        'Clean_Missing': missing_clean,
        'Raw_Missing': missing_raw,
        'Difference': missing_clean - missing_raw
    })
    
    print("各列缺失值对比 (显示缺失值数量变化):")
    print(missing_comparison[missing_comparison['Difference'] != 0])
    
    if (missing_comparison['Clean_Missing'] == 0).all():
        print("\n✓ 清洗文件中无缺失值")
    else:
        print(f"\n⚠️  清洗文件中仍有 {missing_comparison['Clean_Missing'].sum()} 个缺失值")
    
    print("\n" + "="*40)
    print("数据内容初步检查")
    print("="*40)
    
    # 检查共同列是否有相同的值（仅检查前几行作为样本）
    sample_size = min(10, len(df_clean), len(df_raw))
    print(f"检查前 {sample_size} 行数据的一致性:")
    
    for col in list(common_cols)[:5]:  # 限制检查前5个共同列
        if col in df_clean.columns and col in df_raw.columns:
            clean_sample = df_clean[col].head(sample_size).reset_index(drop=True)
            raw_sample = df_raw[col].head(sample_size).reset_index(drop=True)
            
            # 比较前几行的值
            are_equal = clean_sample.equals(raw_sample)
            print(f"  - '{col}': {'相同' if are_equal else '不同'}")
            
            if not are_equal:
                # 显示前几行的差异
                comparison_df = pd.DataFrame({
                    'Raw': raw_sample,
                    'Clean': clean_sample
                })
                print(f"    样本对比 (前{min(5, sample_size)}行):")
                print(comparison_df.head(5))

    print("\n" + "="*40)
    print("总结")
    print("="*40)
    
    total_changes = 0
    if rows_clean != rows_raw:
        total_changes += 1
        print(f"- 行数发生变化: {rows_raw} → {rows_clean}")
    if cols_clean != cols_raw:
        total_changes += 1
        print(f"- 列数发生变化: {cols_raw} → {cols_clean}")
    if len(type_diffs) > 0:
        total_changes += len(type_diffs)
        print(f"- {len(type_diffs)} 列数据类型发生改变")
    if (missing_comparison['Difference'] != 0).any():
        total_changes += (missing_comparison['Difference'] != 0).sum()
        print(f"- 缺失值模式发生变化")
    
    if total_changes == 0:
        print("✓ 两个文件在结构上完全一致")
    else:
        print(f"⚠️  发现 {total_changes} 项主要差异")
    
    print("\n分析完成!")

# 执行比较
compare_csv_files('./data/clean/billionaires_clean.csv', './data/raw/Billionaires Statistics Dataset.csv')



