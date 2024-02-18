def custom_profile(df, features=None, decimal_places=2, datetime_format="%Y-%m-%d"):
    report = {
        'Feature': [],
        'Type': [],
        'Unique': [],
        'Missing%': [],
        'Mean': [],
        'Std Dev': [],
        'Median': [],
        'Min': [],
        'Max': []
    }

    feature_list = df.columns if features is None else features
    for column in feature_list:
        report['Feature'].append(column)
        report['Type'].append(df[column].dtype)
        report['Unique'].append(df[column].nunique())
        report['Missing%'].append(df[column].isnull().mean() * 100)
        if pd.api.types.is_numeric_dtype(df[column]) and not pd.api.types.is_bool_dtype(df[column]):
            mean = df[column].mean()
            std_dev = df[column].std()
            median = df[column].median()
            min_val = df[column].min()
            max_val = df[column].max()
            if any(abs(x) > 1e8 for x in [mean, std_dev, median, min_val, max_val]):
                report['Mean'].append(f'{mean:.2e}')
                report['Std Dev'].append(f'{std_dev:.2e}')
                report['Median'].append(f'{median:.2e}')
                report['Min'].append(f'{min_val:.2e}')
                report['Max'].append(f'{max_val:.2e}')
            else:
                report['Mean'].append(round(mean, 2))
                report['Std Dev'].append(round(std_dev, 2))
                report['Median'].append(round(median, 2))
                report['Min'].append(round(min_val, 2))
                report['Max'].append(round(max_val, 2))
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            report['Mean'].append(df[column].mean().strftime(datetime_format))
            report['Std Dev'].append(None)
            report['Median'].append(df[column].median().strftime(datetime_format))
            report['Min'].append(df[column].min().strftime(datetime_format))
            report['Max'].append(df[column].max().strftime(datetime_format))
        else:
            report['Mean'].append(np.nan)
            report['Std Dev'].append(np.nan)
            report['Median'].append(np.nan)
            report['Min'].append(np.nan)
            report['Max'].append(np.nan)

    report_df = pd.DataFrame(report)

    # Convert float values to string with specific formatting to avoid scientific notation
    float_cols = report_df.select_dtypes(include=['float']).columns
    report_df[float_cols] = report_df[float_cols].apply(lambda x: round(x, decimal_places)).astype(str)
    report_df.replace({np.nan: None}, inplace=True)

    return report_df
