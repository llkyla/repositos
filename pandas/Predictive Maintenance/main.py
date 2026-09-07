# ============================================================
# 제조 설비 Data 기반 고장 예측 및 공정 개선 Point 발굴 Pipeline
# ============================================================

# ============================================================
# 0. Import
# ============================================================

from pathlib import Path

import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu, chi2_contingency
from statsmodels.stats.multitest import multipletests
import statsmodels.api as sm

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    average_precision_score
)


# ============================================================
# 1. Data Load
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "ai4i2020.csv"

print("=" * 60)
print("1. Data Load")
print("=" * 60)

print("Python Path :", Path.cwd())
print("CSV Path    :", DATA_PATH)
print("CSV Exists  :", DATA_PATH.exists())

df = pd.read_csv(DATA_PATH)

print("\nDataset Shape :", df.shape)


# ============================================================
# 2. Base / Data Info
# ============================================================

print("\n" + "=" * 60)
print("2. Base / Data Info")
print("=" * 60)

print("\n[Shape]")
print(df.shape)

print("\n[Columns]")
print(df.columns.tolist())

print("\n[Info]")
df.info()


# ============================================================
# 3. First 5 Rows
# ============================================================

print("\n" + "=" * 60)
print("3. First 5 Rows")
print("=" * 60)

print(df.head())


# ============================================================
# 4. Missing Values
# ============================================================

print("\n" + "=" * 60)
print("4. Missing Values")
print("=" * 60)

missing_df = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Rate": df.isnull().mean()
})

print(missing_df)


# ============================================================
# 5. Duplicated Rows
# ============================================================

print("\n" + "=" * 60)
print("5. Duplicated Rows")
print("=" * 60)

print("Duplicated Rows :", df.duplicated().sum())


# ============================================================
# 6. Descriptive Statistics
# ============================================================

print("\n" + "=" * 60)
print("6. Descriptive Statistics")
print("=" * 60)

print(df.describe(include="all").T)


# ============================================================
# 7. Machine Failure Distribution
# ============================================================

print("\n" + "=" * 60)
print("7. Machine Failure Distribution")
print("=" * 60)

failure_counts = df["Machine failure"].value_counts().sort_index()

print(failure_counts)

print("\nFailure Rate :")
print(df["Machine failure"].mean())


# ============================================================
# 8. Column Information
# ============================================================

print("\n" + "=" * 60)
print("8. Column Information")
print("=" * 60)

column_info = pd.DataFrame({
    "Column": df.columns,
    "Dtype": df.dtypes.astype(str),
    "Unique": df.nunique(),
    "Missing": df.isnull().sum()
})

print(column_info.to_string(index=False))


# ============================================================
# 9. Machine Type Distribution
# ============================================================

print("\n" + "=" * 60)
print("9. Machine Type Distribution")
print("=" * 60)

print(df["Type"].value_counts())


# ============================================================
# 10. Failure Rate by Machine Type
# ============================================================

print("\n" + "=" * 60)
print("10. Failure Rate by Machine Type")
print("=" * 60)

failure_by_type = (
    df.groupby("Type")["Machine failure"]
    .agg(
        Total="count",
        Failure_Count="sum",
        Failure_Rate="mean"
    )
)

print(failure_by_type)


# ============================================================
# 11. Normal vs Failure
# ============================================================

print("\n" + "=" * 60)
print("11. Normal vs Failure")
print("=" * 60)

numeric_compare_cols = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

normal_failure_compare = (
    df.groupby("Machine failure")[numeric_compare_cols]
    .mean()
    .T
)

normal_failure_compare.columns = ["Normal", "Failure"]

print(normal_failure_compare)


# ============================================================
# 12. Failure Rate by Torque
# ============================================================

print("\n" + "=" * 60)
print("12. Failure Rate by Torque")
print("=" * 60)

df["Torque_Zone"] = pd.qcut(
    df["Torque [Nm]"],
    q=10,
    duplicates="drop"
)

torque_failure_rate = (
    df.groupby("Torque_Zone", observed=True)["Machine failure"]
    .agg(
        Total="count",
        Failure_Count="sum",
        Failure_Rate="mean"
    )
)

print(torque_failure_rate)


# ============================================================
# 13. Failure Rate by Tool Wear
# ============================================================

print("\n" + "=" * 60)
print("13. Failure Rate by Tool Wear")
print("=" * 60)

df["Tool_Wear_Zone"] = pd.qcut(
    df["Tool wear [min]"],
    q=10,
    duplicates="drop"
)

tool_wear_failure_rate = (
    df.groupby("Tool_Wear_Zone", observed=True)["Machine failure"]
    .agg(
        Total="count",
        Failure_Count="sum",
        Failure_Rate="mean"
    )
)

print(tool_wear_failure_rate)


# ============================================================
# 14. Failure Type Distribution
# ============================================================

print("\n" + "=" * 60)
print("14. Failure Type Distribution")
print("=" * 60)

failure_type_cols = [
    "TWF",
    "HDF",
    "PWF",
    "OSF",
    "RNF"
]

failure_type_counts = df[failure_type_cols].sum().sort_values(
    ascending=False
)

print(failure_type_counts)

print("\nFailure Type Rate among Machine Failures:")

failure_only = df[df["Machine failure"] == 1]

failure_type_rate = (
    failure_only[failure_type_cols]
    .sum()
    .sort_values(ascending=False)
    / len(failure_only)
)

print(failure_type_rate)


# ============================================================
# 15. Failure Type Specific Feature Comparison
# ============================================================

print("\n" + "=" * 60)
print("15. Failure Type Specific Feature Comparison")
print("=" * 60)

failure_type_feature_summary = {}

for failure_type in failure_type_cols:

    failure_type_feature_summary[failure_type] = {}

    for col in numeric_compare_cols:

        failure_group = df.loc[df[failure_type] == 1, col]
        normal_group = df.loc[df[failure_type] == 0, col]

        failure_type_feature_summary[failure_type][col] = {
            "Failure_Type_Mean": failure_group.mean(),
            "Non_Failure_Type_Mean": normal_group.mean(),
            "Difference": (
                failure_group.mean() -
                normal_group.mean()
            )
        }

for failure_type, result in failure_type_feature_summary.items():

    print(f"\n[{failure_type}]")

    for feature, values in result.items():

        print(
            f"{feature} | "
            f"Type Mean={values['Failure_Type_Mean']:.4f} | "
            f"Other Mean={values['Non_Failure_Type_Mean']:.4f} | "
            f"Diff={values['Difference']:.4f}"
        )


# ============================================================
# 16. Failure Type by Machine Type
# ============================================================

print("\n" + "=" * 60)
print("16. Failure Type by Machine Type")
print("=" * 60)

failure_type_by_machine = (
    df.groupby("Type")[failure_type_cols]
    .sum()
)

print(failure_type_by_machine)

print("\n[Failure Type Rate within Machine Type]")

failure_type_rate_by_machine = (
    df.groupby("Type")[failure_type_cols]
    .mean()
)

print(failure_type_rate_by_machine)


# ============================================================
# 17. Failure Type and Temperature
# ============================================================

print("\n" + "=" * 60)
print("17. Failure Type and Temperature")
print("=" * 60)

df["Temperature_Diff"] = (
    df["Process temperature [K]"]
    - df["Air temperature [K]"]
)

temperature_cols = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Temperature_Diff"
]

for failure_type in failure_type_cols:

    print(f"\n[{failure_type}]")

    print(
        df.groupby(failure_type)[temperature_cols]
        .mean()
    )


# ============================================================
# 18. Failure Type and Tool Wear
# ============================================================

print("\n" + "=" * 60)
print("18. Failure Type and Tool Wear")
print("=" * 60)

for failure_type in failure_type_cols:

    print(f"\n[{failure_type}]")

    print(
        df.groupby(failure_type)["Tool wear [min]"]
        .mean()
    )


# ============================================================
# 19. Failure Type and Power
# ============================================================

print("\n" + "=" * 60)
print("19. Failure Type and Power")
print("=" * 60)

df["Power [W]"] = (
    df["Torque [Nm]"]
    * df["Rotational speed [rpm]"]
    * (2 * np.pi / 60)
)

for failure_type in failure_type_cols:

    print(f"\n[{failure_type}]")

    print(
        df.groupby(failure_type)["Power [W]"]
        .mean()
    )


# ============================================================
# 20. Failure Type and Overstrain
# ============================================================

print("\n" + "=" * 60)
print("20. Failure Type and Overstrain")
print("=" * 60)

df["Torque_Wear_Interaction"] = (
    df["Torque [Nm]"]
    * df["Tool wear [min]"]
)

for failure_type in failure_type_cols:

    print(f"\n[{failure_type}]")

    print(
        df.groupby(failure_type)[
            [
                "Torque [Nm]",
                "Tool wear [min]",
                "Torque_Wear_Interaction"
            ]
        ].mean()
    )


# ============================================================
# 21. Failure Type Correlation
# ============================================================

print("\n" + "=" * 60)
print("21. Failure Type Correlation")
print("=" * 60)

correlation_cols = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Temperature_Diff",
    "Power [W]",
    "Torque_Wear_Interaction"
]

failure_type_correlation = (
    df[correlation_cols + failure_type_cols]
    .corr()[failure_type_cols]
    .loc[correlation_cols]
)

print(failure_type_correlation)


# ============================================================
# 22. Top Related Features by Failure Type
# ============================================================

print("\n" + "=" * 60)
print("22. Top Related Features by Failure Type")
print("=" * 60)

for failure_type in failure_type_cols:

    print(f"\n[{failure_type}]")

    top_corr = (
        failure_type_correlation[failure_type]
        .abs()
        .sort_values(ascending=False)
        .head(5)
    )

    print(top_corr)


# ============================================================
# 23. Failure Type Co-occurrence
# ============================================================

print("\n" + "=" * 60)
print("23. Failure Type Co-occurrence")
print("=" * 60)

co_occurrence = pd.DataFrame(
    index=failure_type_cols,
    columns=failure_type_cols,
    dtype=int
)

for col1 in failure_type_cols:
    for col2 in failure_type_cols:

        co_occurrence.loc[col1, col2] = (
            (df[col1] == 1) &
            (df[col2] == 1)
        ).sum()

print(co_occurrence)


# ============================================================
# 24. Multiple Failure Type Cases
# ============================================================

print("\n" + "=" * 60)
print("24. Multiple Failure Type Cases")
print("=" * 60)

df["Failure_Type_Count"] = df[failure_type_cols].sum(axis=1)

print(
    df["Failure_Type_Count"]
    .value_counts()
    .sort_index()
)

print("\nMultiple Failure Type Cases:")

print(
    df[df["Failure_Type_Count"] >= 2][
        [
            "UDI",
            "Product ID",
            "Type",
            "Machine failure"
        ] + failure_type_cols
    ].head(20)
)


# ============================================================
# 25. Failure Type Key Feature Summary
# ============================================================

print("\n" + "=" * 60)
print("25. Failure Type Key Feature Summary")
print("=" * 60)

failure_type_key_features = {
    "TWF": [
        "Tool wear [min]"
    ],
    "HDF": [
        "Air temperature [K]",
        "Temperature_Diff"
    ],
    "PWF": [
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Power [W]"
    ],
    "OSF": [
        "Torque [Nm]",
        "Tool wear [min]",
        "Torque_Wear_Interaction"
    ],
    "RNF": [
        "RNF count is too small for reliable interpretation"
    ]
}

for failure_type, features in failure_type_key_features.items():

    print(f"{failure_type} : {features}")


# ============================================================
# 26. Statistical Analysis Preparation
# ============================================================

print("\n" + "=" * 60)
print("26. Statistical Analysis Preparation")
print("=" * 60)

print("Mann-Whitney U Test + Effect Size")
print("Chi-square Test + FDR Correction")


# ============================================================
# 27. Statistical Significance Test
# ============================================================

print("\n" + "=" * 60)
print("27. Statistical Significance Test")
print("=" * 60)

stat_features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Temperature_Diff",
    "Power [W]",
    "Torque_Wear_Interaction"
]

mannwhitney_results = []

for failure_type in failure_type_cols:

    for feature in stat_features:

        group_1 = df.loc[df[failure_type] == 1, feature]
        group_0 = df.loc[df[failure_type] == 0, feature]

        if len(group_1) == 0:
            continue

        stat, p_value = mannwhitneyu(
            group_1,
            group_0,
            alternative="two-sided"
        )

        mannwhitney_results.append({
            "Failure_Type": failure_type,
            "Feature": feature,
            "U_Statistic": stat,
            "P_Value": p_value
        })

mannwhitney_df = pd.DataFrame(mannwhitney_results)

print(
    mannwhitney_df
    .sort_values("P_Value")
    .to_string(index=False)
)


# ============================================================
# 28. Effect Size
# ============================================================

print("\n" + "=" * 60)
print("28. Effect Size")
print("=" * 60)

effect_results = []

for _, row in mannwhitney_df.iterrows():

    failure_type = row["Failure_Type"]
    feature = row["Feature"]

    group_1 = df.loc[df[failure_type] == 1, feature]
    group_0 = df.loc[df[failure_type] == 0, feature]

    n1 = len(group_1)
    n0 = len(group_0)

    U = row["U_Statistic"]

    effect_size = (
        2 * U / (n1 * n0)
    ) - 1

    effect_results.append({
        "Failure_Type": failure_type,
        "Feature": feature,
        "Effect_Size": abs(effect_size),
        "P_Value": row["P_Value"]
    })

effect_df = pd.DataFrame(effect_results)

print(
    effect_df
    .sort_values(
        ["Failure_Type", "Effect_Size"],
        ascending=[True, False]
    )
    .to_string(index=False)
)


# ============================================================
# 29. Chi-square Test
# ============================================================

print("\n" + "=" * 60)
print("29. Chi-square Test")
print("=" * 60)

chi_results = []

for failure_type in failure_type_cols:

    contingency = pd.crosstab(
        df["Type"],
        df[failure_type]
    )

    chi2, p_value, dof, expected = chi2_contingency(
        contingency
    )

    chi_results.append({
        "Failure_Type": failure_type,
        "Chi2": chi2,
        "P_Value": p_value,
        "DOF": dof
    })

chi_df = pd.DataFrame(chi_results)

print(chi_df)


# ============================================================
# 30. Multiple Testing Correction + Root Cause Summary
# ============================================================

print("\n" + "=" * 60)
print("30. Multiple Testing Correction + Root Cause Summary")
print("=" * 60)

# FDR correction
reject, p_adjusted, _, _ = multipletests(
    mannwhitney_df["P_Value"],
    method="fdr_bh"
)

mannwhitney_df["P_Adjusted"] = p_adjusted
mannwhitney_df["Significant"] = reject

print("\n[FDR Corrected Mann-Whitney Results]")

significant_results = (
    mannwhitney_df[
        mannwhitney_df["Significant"]
    ]
    .merge(
        effect_df[
            [
                "Failure_Type",
                "Feature",
                "Effect_Size"
            ]
        ],
        on=["Failure_Type", "Feature"],
        how="left"
    )
    .sort_values(
        ["Failure_Type", "Effect_Size"],
        ascending=[True, False]
    )
)

print(significant_results.to_string(index=False))


# Chi-square FDR
chi_reject, chi_adjusted, _, _ = multipletests(
    chi_df["P_Value"],
    method="fdr_bh"
)

chi_df["P_Adjusted"] = chi_adjusted
chi_df["Significant"] = chi_reject

print("\n[FDR Corrected Chi-square]")

print(chi_df)


# Root cause candidate summary
root_cause_candidates = (
    significant_results
    .sort_values(
        ["Failure_Type", "Effect_Size"],
        ascending=[True, False]
    )
    .groupby("Failure_Type")
    .head(3)
)

print("\n[Root Cause Candidate Summary]")

print(
    root_cause_candidates[
        [
            "Failure_Type",
            "Feature",
            "Effect_Size",
            "P_Adjusted"
        ]
    ].to_string(index=False)
)


# ============================================================
# 31. Multivariate & Interaction Risk Zone Analysis
# ============================================================

print("\n" + "=" * 60)
print("31. Multivariate & Interaction Risk Zone Analysis")
print("=" * 60)

# ----------------------------
# OSF
# High Torque + High Tool Wear
# ----------------------------

high_torque = df["Torque [Nm]"] >= 52
high_tool_wear = df["Tool wear [min]"] >= 195

df["High_Torque_High_Wear"] = (
    high_torque &
    high_tool_wear
).astype(int)

osf_zone = df[
    (high_torque) &
    (high_tool_wear)
]

print("\n[OSF: High Torque + High Tool Wear]")

print(
    "Machines       :", len(osf_zone)
)

print(
    "Failures       :",
    osf_zone["Machine failure"].sum()
)

print(
    "Failure Rate   :",
    osf_zone["Machine failure"].mean()
)


# ----------------------------
# HDF
# High Air Temperature
# + Low Temperature Difference
# ----------------------------

high_air_temp = df["Air temperature [K]"] >= 301
low_temp_diff = df["Temperature_Diff"] <= 9

df["High_AirTemp_Low_TempDiff"] = (
    high_air_temp &
    low_temp_diff
).astype(int)

hdf_zone = df[
    (high_air_temp) &
    (low_temp_diff)
]

print("\n[HDF: High Air Temp + Low Temp Diff]")

print(
    "Machines       :", len(hdf_zone)
)

print(
    "Failures       :",
    hdf_zone["Machine failure"].sum()
)

print(
    "Failure Rate   :",
    hdf_zone["Machine failure"].mean()
)


# ----------------------------
# PWF
# Low RPM + High Torque
# ----------------------------

low_rpm = df["Rotational speed [rpm]"] <= 1400
high_torque_pwf = df["Torque [Nm]"] >= 45

df["High_RPM_High_Torque"] = (
    (df["Rotational speed [rpm]"] >= 1700) &
    (df["Torque [Nm]"] >= 45)
).astype(int)

pwf_zone = df[
    (low_rpm) &
    (high_torque_pwf)
]

print("\n[PWF: Low RPM + High Torque]")

print(
    "Machines       :", len(pwf_zone)
)

print(
    "Failures       :",
    pwf_zone["Machine failure"].sum()
)

print(
    "Failure Rate   :",
    pwf_zone["Machine failure"].mean()
)


# ============================================================
# 32. Interaction Logistic Regression
# ============================================================

print("\n" + "=" * 60)
print("32. Interaction Logistic Regression")
print("=" * 60)

# OSF interaction
osf_interaction_df = df[
    [
        "Machine failure",
        "Torque [Nm]",
        "Tool wear [min]"
    ]
].copy()

osf_interaction_df["Torque_std"] = (
    osf_interaction_df["Torque [Nm]"]
    - osf_interaction_df["Torque [Nm]"].mean()
) / osf_interaction_df["Torque [Nm]"].std()

osf_interaction_df["Tool_Wear_std"] = (
    osf_interaction_df["Tool wear [min]"]
    - osf_interaction_df["Tool wear [min]"].mean()
) / osf_interaction_df["Tool wear [min]"].std()

osf_interaction_df["Interaction"] = (
    osf_interaction_df["Torque_std"]
    * osf_interaction_df["Tool_Wear_std"]
)

X_osf = sm.add_constant(
    osf_interaction_df[
        [
            "Torque_std",
            "Tool_Wear_std",
            "Interaction"
        ]
    ]
)

y_osf = osf_interaction_df["Machine failure"]

osf_logit = sm.Logit(
    y_osf,
    X_osf
).fit(disp=False)

print("\n[OSF Interaction Logistic Regression]")

print(osf_logit.summary())

interaction_coef = osf_logit.params["Interaction"]
interaction_p = osf_logit.pvalues["Interaction"]

print("\nInteraction Coefficient :", interaction_coef)
print("Interaction Odds Ratio :", np.exp(interaction_coef))
print("Interaction P-Value    :", interaction_p)


# HDF interaction
hdf_interaction_df = df[
    [
        "Machine failure",
        "Air temperature [K]",
        "Temperature_Diff"
    ]
].copy()

hdf_interaction_df["Air_std"] = (
    hdf_interaction_df["Air temperature [K]"]
    - hdf_interaction_df["Air temperature [K]"].mean()
) / hdf_interaction_df["Air temperature [K]"].std()

hdf_interaction_df["TempDiff_std"] = (
    hdf_interaction_df["Temperature_Diff"]
    - hdf_interaction_df["Temperature_Diff"].mean()
) / hdf_interaction_df["Temperature_Diff"].std()

hdf_interaction_df["Interaction"] = (
    hdf_interaction_df["Air_std"]
    * hdf_interaction_df["TempDiff_std"]
)

X_hdf = sm.add_constant(
    hdf_interaction_df[
        [
            "Air_std",
            "TempDiff_std",
            "Interaction"
        ]
    ]
)

y_hdf = hdf_interaction_df["Machine failure"]

hdf_logit = sm.Logit(
    y_hdf,
    X_hdf
).fit(disp=False)

print("\n[HDF Interaction Logistic Regression]")

print(hdf_logit.summary())


# PWF interaction
pwf_interaction_df = df[
    [
        "Machine failure",
        "Rotational speed [rpm]",
        "Torque [Nm]"
    ]
].copy()

pwf_interaction_df["RPM_std"] = (
    pwf_interaction_df["Rotational speed [rpm]"]
    - pwf_interaction_df["Rotational speed [rpm]"].mean()
) / pwf_interaction_df["Rotational speed [rpm]"].std()

pwf_interaction_df["Torque_std"] = (
    pwf_interaction_df["Torque [Nm]"]
    - pwf_interaction_df["Torque [Nm]"].mean()
) / pwf_interaction_df["Torque [Nm]"].std()

pwf_interaction_df["Interaction"] = (
    pwf_interaction_df["RPM_std"]
    * pwf_interaction_df["Torque_std"]
)

X_pwf = sm.add_constant(
    pwf_interaction_df[
        [
            "RPM_std",
            "Torque_std",
            "Interaction"
        ]
    ]
)

y_pwf = pwf_interaction_df["Machine failure"]

pwf_logit = sm.Logit(
    y_pwf,
    X_pwf
).fit(disp=False)

print("\n[PWF Interaction Logistic Regression]")

print(pwf_logit.summary())


# ============================================================
# 33. Interaction Result Summary / Risk Zone Ranking
# ============================================================

print("\n" + "=" * 60)
print("33. Interaction Result Summary / Risk Zone Ranking")
print("=" * 60)

interaction_summary = pd.DataFrame({
    "Failure_Type": [
        "OSF",
        "HDF",
        "PWF"
    ],
    "Interaction": [
        "Torque × Tool Wear",
        "Air Temperature × Temperature Diff",
        "RPM × Torque"
    ],
    "Odds_Ratio": [
        np.exp(
            osf_logit.params["Interaction"]
        ),
        np.exp(
            hdf_logit.params["Interaction"]
        ),
        np.exp(
            pwf_logit.params["Interaction"]
        )
    ],
    "P_Value": [
        osf_logit.pvalues["Interaction"],
        hdf_logit.pvalues["Interaction"],
        pwf_logit.pvalues["Interaction"]
    ]
})

interaction_summary["Significant"] = (
    interaction_summary["P_Value"] < 0.05
)

print(interaction_summary)


# ============================================================
# 34. Feature Engineering
# ============================================================

print("\n" + "=" * 60)
print("34. Feature Engineering")
print("=" * 60)

# ----------------------------
# Continuous Features
# ----------------------------

df["RPM_Torque_Interaction"] = (
    df["Rotational speed [rpm]"]
    * df["Torque [Nm]"]
)

df["Torque_RPM_Ratio"] = (
    df["Torque [Nm]"]
    / (df["Rotational speed [rpm]"] + 1e-6)
)

df["Process_Air_Temp_Ratio"] = (
    df["Process temperature [K]"]
    / (df["Air temperature [K]"] + 1e-6)
)


# ----------------------------
# Quantile Zones
# ----------------------------

df["Air_Temp_Zone"] = pd.qcut(
    df["Air temperature [K]"],
    q=10,
    duplicates="drop"
)

df["RPM_Zone"] = pd.qcut(
    df["Rotational speed [rpm]"],
    q=10,
    duplicates="drop"
)

df["Temp_Diff_Zone"] = pd.qcut(
    df["Temperature_Diff"],
    q=10,
    duplicates="drop"
)


# ----------------------------
# Machine Type One-Hot Encoding
# ----------------------------

type_dummies = pd.get_dummies(
    df["Type"],
    prefix="Type",
    dtype=int
)

for machine_type in ["H", "L", "M"]:

    col = f"Type_{machine_type}"

    if col not in type_dummies.columns:
        type_dummies[col] = 0

df = pd.concat(
    [
        df,
        type_dummies[
            [
                "Type_H",
                "Type_L",
                "Type_M"
            ]
        ]
    ],
    axis=1
)


# ============================================================
# 35. Machine Failure Prediction
# ============================================================

print("\n" + "=" * 60)
print("35. Machine Failure Prediction")
print("=" * 60)

feature_cols = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Temperature_Diff",
    "Power [W]",
    "Torque_Wear_Interaction",
    "RPM_Torque_Interaction",
    "Torque_RPM_Ratio",
    "Process_Air_Temp_Ratio",
    "Torque_Zone",
    "Tool_Wear_Zone",
    "Air_Temp_Zone",
    "RPM_Zone",
    "Temp_Diff_Zone",
    "High_Torque_High_Wear",
    "High_AirTemp_Low_TempDiff",
    "High_RPM_High_Torque",
    "Type_H",
    "Type_L",
    "Type_M"
]


# Category → numeric encoding
ml_df = df.copy()

zone_cols = [
    "Torque_Zone",
    "Tool_Wear_Zone",
    "Air_Temp_Zone",
    "RPM_Zone",
    "Temp_Diff_Zone"
]

for col in zone_cols:

    ml_df[col] = (
        ml_df[col]
        .cat.codes
    )


# Safe feature names for XGBoost
safe_feature_names = {
    "Air temperature [K]": "Air_Temperature",
    "Process temperature [K]": "Process_Temperature",
    "Rotational speed [rpm]": "Rotational_Speed",
    "Torque [Nm]": "Torque",
    "Tool wear [min]": "Tool_Wear",
    "Temperature_Diff": "Temperature_Diff",
    "Power [W]": "Power",
    "Torque_Wear_Interaction": "Torque_Wear_Interaction",
    "RPM_Torque_Interaction": "RPM_Torque_Interaction",
    "Torque_RPM_Ratio": "Torque_RPM_Ratio",
    "Process_Air_Temp_Ratio": "Process_Air_Temp_Ratio",
    "Torque_Zone": "Torque_Zone",
    "Tool_Wear_Zone": "Tool_Wear_Zone",
    "Air_Temp_Zone": "Air_Temp_Zone",
    "RPM_Zone": "RPM_Zone",
    "Temp_Diff_Zone": "Temp_Diff_Zone",
    "High_Torque_High_Wear": "High_Torque_High_Wear",
    "High_AirTemp_Low_TempDiff": "High_AirTemp_Low_TempDiff",
    "High_RPM_High_Torque": "High_RPM_High_Torque",
    "Type_H": "Type_H",
    "Type_L": "Type_L",
    "Type_M": "Type_M"
}

X = (
    ml_df[feature_cols]
    .copy()
    .rename(columns=safe_feature_names)
)

y = ml_df["Machine failure"]


# ----------------------------
# Model Selection
# ----------------------------

try:

    from xgboost import XGBClassifier

    MODEL_NAME = "XGBoost"

    def create_model(scale_pos_weight=None):

        params = {
            "n_estimators": 300,
            "max_depth": 5,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "random_state": 42,
            "eval_metric": "logloss"
        }

        if scale_pos_weight is not None:
            params["scale_pos_weight"] = scale_pos_weight

        return XGBClassifier(**params)


except ImportError:

    from sklearn.ensemble import RandomForestClassifier

    MODEL_NAME = "RandomForest"

    def create_model(scale_pos_weight=None):

        return RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            min_samples_leaf=3,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )


print("Model :", MODEL_NAME)


# ----------------------------
# Train / Test Split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scale_pos_weight = (
    (y_train == 0).sum()
    / (y_train == 1).sum()
)

print("\n[Train Distribution]")

print(
    y_train.value_counts()
    .sort_index()
)

print(
    "\nScale Pos Weight :",
    scale_pos_weight
)


# ----------------------------
# Model Train
# ----------------------------

model = create_model(
    scale_pos_weight=scale_pos_weight
)

model.fit(
    X_train,
    y_train
)


# ----------------------------
# Evaluation
# ----------------------------

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\n[Classification Report]")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Normal",
            "Failure"
        ]
    )
)

print("\n[Confusion Matrix]")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

pr_auc = average_precision_score(
    y_test,
    y_prob
)

print("\nROC-AUC :", roc_auc)
print("PR-AUC  :", pr_auc)


# ----------------------------
# Feature Importance
# ----------------------------

feature_importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(
    "Importance",
    ascending=False
)

print("\n[Top 20 Feature Importance]")

print(
    feature_importance_df
    .head(20)
    .to_string(index=False)
)


# ============================================================
# 36. Failure Type Prediction
# ============================================================

print("\n" + "=" * 60)
print("36. Failure Type Prediction")
print("=" * 60)

failure_type_models = {}
failure_type_probabilities = {}

for failure_type in [
    "TWF",
    "HDF",
    "PWF",
    "OSF"
]:

    print("\n" + "-" * 50)
    print(f"Failure Type : {failure_type}")
    print("-" * 50)

    y_type = ml_df[failure_type]

    X_train_type, X_test_type, y_train_type, y_test_type = (
        train_test_split(
            X,
            y_type,
            test_size=0.2,
            random_state=42,
            stratify=y_type
        )
    )

    type_scale_pos_weight = (
        (y_train_type == 0).sum()
        / max((y_train_type == 1).sum(), 1)
    )

    type_model = create_model(
        scale_pos_weight=type_scale_pos_weight
    )

    type_model.fit(
        X_train_type,
        y_train_type
    )

    type_pred = type_model.predict(
        X_test_type
    )

    type_prob = type_model.predict_proba(
        X_test_type
    )[:, 1]

    print(
        classification_report(
            y_test_type,
            type_pred,
            target_names=[
                "Other",
                failure_type
            ],
            zero_division=0
        )
    )

    print(
        "ROC-AUC :",
        roc_auc_score(
            y_test_type,
            type_prob
        )
    )

    print(
        "PR-AUC  :",
        average_precision_score(
            y_test_type,
            type_prob
        )
    )

    # Full Dataset Probability
    full_type_prob = type_model.predict_proba(
        X
    )[:, 1]

    failure_type_models[
        failure_type
    ] = type_model

    failure_type_probabilities[
        failure_type
    ] = full_type_prob


# ============================================================
# 37. SHAP Analysis
# ============================================================

print("\n" + "=" * 60)
print("37. SHAP Analysis")
print("=" * 60)

try:

    import shap

    # ----------------------------
    # Machine Failure SHAP
    # ----------------------------

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    if isinstance(shap_values, list):
        shap_array = np.asarray(
            shap_values[-1]
        )
    else:
        shap_array = np.asarray(
            shap_values
        )

    if shap_array.ndim == 3:
        shap_array = shap_array[:, :, -1]

    machine_shap_importance = pd.DataFrame({
        "Feature": X.columns,
        "Mean_Abs_SHAP": np.abs(
            shap_array
        ).mean(axis=0)
    }).sort_values(
        "Mean_Abs_SHAP",
        ascending=False
    )

    print("\n[Machine Failure SHAP]")

    print(
        machine_shap_importance
        .head(20)
        .to_string(index=False)
    )


    # ----------------------------
    # Failure Type SHAP
    # ----------------------------

    failure_type_shap_summary = {}

    for failure_type, type_model in failure_type_models.items():

        type_explainer = shap.TreeExplainer(
            type_model
        )

        type_shap_values = (
            type_explainer.shap_values(X)
        )

        if isinstance(type_shap_values, list):

            type_shap_array = np.asarray(
                type_shap_values[-1]
            )

        else:

            type_shap_array = np.asarray(
                type_shap_values
            )

        if type_shap_array.ndim == 3:

            type_shap_array = (
                type_shap_array[:, :, -1]
            )

        type_shap_importance = pd.DataFrame({
            "Feature": X.columns,
            "Mean_Abs_SHAP": np.abs(
                type_shap_array
            ).mean(axis=0)
        }).sort_values(
            "Mean_Abs_SHAP",
            ascending=False
        )

        failure_type_shap_summary[
            failure_type
        ] = type_shap_importance

        print(
            f"\n[{failure_type} SHAP]"
        )

        print(
            type_shap_importance
            .head(15)
            .to_string(index=False)
        )


except ImportError:

    print(
        "\nSHAP is not installed."
    )

    print(
        "Install with: pip install shap"
    )

    machine_shap_importance = pd.DataFrame()


# ============================================================
# 38. Model Interpretation Summary
# ============================================================

print("\n" + "=" * 60)
print("38. Model Interpretation Summary")
print("=" * 60)

if not machine_shap_importance.empty:

    print(
        "\n[Top Machine Failure Risk Factors]"
    )

    print(
        machine_shap_importance
        .head(10)
        .to_string(index=False)
    )

print(
    "\n[Interpretation]"
)

print(
    "Machine Failure 예측에서는 "
    "Tool Wear, Power, Rotational Speed, "
    "Torque 관련 파생변수가 주요 위험 요인으로 확인됨."
)

print(
    "Failure Type별로는 "
    "TWF → Tool Wear, "
    "HDF → Temperature 조건, "
    "PWF → RPM/Power/Torque, "
    "OSF → Torque + Tool Wear 조합이 핵심 후보로 확인됨."
)


# ============================================================
# 39. Risk Score
# ============================================================

print("\n" + "=" * 60)
print("39. Risk Score")
print("=" * 60)

# Full dataset operational risk scoring
failure_prob = model.predict_proba(
    X
)[:, 1]

risk_df = df.copy()

risk_df["Failure_Probability"] = failure_prob

risk_df["Risk_Score"] = (
    risk_df["Failure_Probability"]
    * 100
)

print(
    risk_df["Risk_Score"]
    .describe()
)

print("\n[Top 20 Risk Machines]")

print(
    risk_df[
        [
            "UDI",
            "Product ID",
            "Type",
            "Machine failure",
            "Failure_Probability",
            "Risk_Score"
        ]
    ]
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .head(20)
    .to_string(index=False)
)


# ============================================================
# 40. Risk Level & Failure Type & Action Rule
# ============================================================

print("\n" + "=" * 60)
print("40. Risk Level & Failure Type & Action Rule")
print("=" * 60)


# ----------------------------
# 40-1. Risk Level
# ----------------------------

def get_risk_level(score):

    if score >= 70:
        return "Critical"

    elif score >= 40:
        return "High"

    elif score >= 20:
        return "Medium"

    else:
        return "Low"


risk_df["Risk_Level"] = (
    risk_df["Risk_Score"]
    .apply(get_risk_level)
)

print("\n[Risk Level]")

print(
    risk_df["Risk_Level"]
    .value_counts()
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],
        fill_value=0
    )
)


# ----------------------------
# 40-2. Failure Type Probability
# ----------------------------

for failure_type in [
    "TWF",
    "HDF",
    "PWF",
    "OSF"
]:

    risk_df[
        f"{failure_type}_Probability"
    ] = failure_type_probabilities[
        failure_type
    ]


failure_probability_columns = [
    "TWF_Probability",
    "HDF_Probability",
    "PWF_Probability",
    "OSF_Probability"
]

risk_df["Max_Failure_Type_Probability"] = (
    risk_df[
        failure_probability_columns
    ].max(axis=1)
)

risk_df["Predicted_Failure_Type"] = (
    risk_df[
        failure_probability_columns
    ]
    .idxmax(axis=1)
    .str.replace(
        "_Probability",
        "",
        regex=False
    )
)

# Machine Failure Probability가 낮으면
# 특정 Failure Type을 강제로 지정하지 않음
risk_df.loc[
    risk_df["Failure_Probability"] < 0.20,
    "Predicted_Failure_Type"
] = "Normal"


# ----------------------------
# 40-3. Key Risk Factor
# ----------------------------

def get_risk_factor(row):

    failure_type = row[
        "Predicted_Failure_Type"
    ]

    torque = row["Torque [Nm]"]
    tool_wear = row["Tool wear [min]"]
    air_temp = row["Air temperature [K]"]
    temp_diff = row["Temperature_Diff"]
    rpm = row["Rotational speed [rpm]"]

    if failure_type == "OSF":

        if (
            torque >= 52
            and tool_wear >= 195
        ):
            return "High Torque + High Tool Wear"

        elif torque >= 52:
            return "High Torque"

        elif tool_wear >= 195:
            return "High Tool Wear"

        else:
            return "Load / Wear Condition"

    elif failure_type == "TWF":

        if tool_wear >= 195:
            return "High Tool Wear"

        else:
            return "Tool Wear"

    elif failure_type == "HDF":

        if (
            air_temp >= 301
            and temp_diff <= 9
        ):
            return "High Air Temp + Low Temp Diff"

        else:
            return "Temperature Condition"

    elif failure_type == "PWF":

        if (
            rpm >= 1700
            and torque >= 45
        ):
            return "High RPM + High Torque"

        elif torque >= 45:
            return "High Torque"

        elif rpm >= 1700:
            return "High RPM"

        else:
            return "Power Condition"

    else:

        return "No Major Risk"


risk_df["Key_Risk_Factor"] = (
    risk_df.apply(
        get_risk_factor,
        axis=1
    )
)


# ----------------------------
# 40-4. Recommended Action
# ----------------------------

def get_recommended_action(row):

    risk_level = row[
        "Risk_Level"
    ]

    factor = row[
        "Key_Risk_Factor"
    ]

    if risk_level == "Critical":

        return (
            f"즉시 점검 - {factor}"
        )

    elif risk_level == "High":

        return (
            f"우선 점검 - {factor}"
        )

    elif risk_level == "Medium":

        return (
            f"추세 모니터링 - {factor}"
        )

    else:

        return "정상 모니터링"


risk_df["Recommended_Action"] = (
    risk_df.apply(
        get_recommended_action,
        axis=1
    )
)


# ============================================================
# 40-5. Risk Level Summary
# ============================================================

print("\n[Risk Level Summary]")

print(
    risk_df[
        [
            "Risk_Level",
            "Machine failure"
        ]
    ]
    .groupby("Risk_Level")
    .agg(
        Machines=("Machine failure", "count"),
        Actual_Failures=("Machine failure", "sum"),
        Avg_Risk_Score=(
            "Risk_Level",
            lambda x: risk_df.loc[
                x.index,
                "Risk_Score"
            ].mean()
        )
    )
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )
)


# ============================================================
# 40-6. Predicted Failure Type Summary
# ============================================================

print("\n[Predicted Failure Type]")

print(
    risk_df[
        "Predicted_Failure_Type"
    ]
    .value_counts()
)


# ============================================================
# 40-7. Recommended Action Summary
# ============================================================

print("\n[Recommended Action]")

print(
    risk_df[
        "Recommended_Action"
    ]
    .value_counts()
)


# ============================================================
# 40-8. Improvement Point
# ============================================================

print("\n" + "=" * 60)
print("40-8. Improvement Point")
print("=" * 60)


# ----------------------------
# Improvement Failure Type
# ----------------------------

risk_df["Improvement_Failure_Type"] = (
    risk_df["Predicted_Failure_Type"]
)


# ----------------------------
# Improvement Point
# ----------------------------

def get_improvement_point(row):

    failure_type = row["Predicted_Failure_Type"]

    torque = row["Torque [Nm]"]
    tool_wear = row["Tool wear [min]"]
    air_temp = row["Air temperature [K]"]
    temp_diff = row["Temperature_Diff"]
    rpm = row["Rotational speed [rpm]"]

    if failure_type == "OSF":

        if torque >= 52 and tool_wear >= 195:
            return "Torque + Tool Wear"

        elif torque >= 52:
            return "High Torque"

        elif tool_wear >= 195:
            return "High Tool Wear"

        else:
            return "Load / Wear"

    elif failure_type == "TWF":

        if tool_wear >= 195:
            return "High Tool Wear"

        else:
            return "Tool Wear"

    elif failure_type == "HDF":

        if air_temp >= 301 and temp_diff <= 9:
            return "High Air Temp + Low Temp Diff"

        else:
            return "Temperature Condition"

    elif failure_type == "PWF":

        if rpm >= 1700 and torque >= 45:
            return "RPM + Torque"

        elif torque >= 45:
            return "High Torque"

        elif rpm >= 1700:
            return "High RPM"

        else:
            return "Power Condition"

    else:
        return "No Major Risk"


risk_df["Improvement_Point"] = (
    risk_df.apply(
        get_improvement_point,
        axis=1
    )
)


# ----------------------------
# Improvement Goal
# ----------------------------

def get_improvement_goal(row):

    point = row["Improvement_Point"]

    if point == "Torque + Tool Wear":
        return "고부하 상태에서 공구 마모 동시 관리"

    elif point == "High Torque":
        return "고토크 운전 조건 관리"

    elif point == "High Tool Wear":
        return "공구 마모 및 교체주기 관리"

    elif point == "High Air Temp + Low Temp Diff":
        return "열환경 및 냉각 조건 관리"

    elif point == "Temperature Condition":
        return "온도 변화 추세 관리"

    elif point == "RPM + Torque":
        return "고속·고토크 동시 운전 관리"

    elif point == "High RPM":
        return "고속 회전 조건 관리"

    elif point == "Power Condition":
        return "Power / RPM / Torque 조건 관리"

    elif point == "Load / Wear":
        return "부하 및 공구 마모 추세 관리"

    elif point == "Tool Wear":
        return "공구 마모 추세 관리"

    else:
        return "정상 상태 유지 및 모니터링"


risk_df["Improvement_Goal"] = (
    risk_df.apply(
        get_improvement_goal,
        axis=1
    )
)


# ----------------------------
# Control Action
# ----------------------------

def get_control_action(row):

    point = row["Improvement_Point"]

    if point == "Torque + Tool Wear":
        return "Torque 및 Tool Wear 동시 모니터링"

    elif point == "High Torque":
        return "Torque 추세 및 고토크 발생 구간 모니터링"

    elif point == "High Tool Wear":
        return "Tool Wear 추세 및 공구 교체주기 모니터링"

    elif point == "High Air Temp + Low Temp Diff":
        return "Air Temperature 및 Temperature Diff 동시 관리"

    elif point == "Temperature Condition":
        return "온도 변화 추세 모니터링"

    elif point == "RPM + Torque":
        return "RPM 및 Torque 동시 모니터링"

    elif point == "High RPM":
        return "고속 회전 조건 모니터링"

    elif point == "Power Condition":
        return "Power / RPM / Torque 동시 모니터링"

    elif point == "Load / Wear":
        return "부하 및 공구 마모 추세 모니터링"

    elif point == "Tool Wear":
        return "Tool Wear 추세 모니터링"

    else:
        return "정상 상태 모니터링"


# ★ 중요: 반드시 axis=1
risk_df["Control_Action"] = (
    risk_df.apply(
        get_control_action,
        axis=1
    )
)


# ----------------------------
# Improvement Priority
# ----------------------------

def get_improvement_priority(row):

    point = row["Improvement_Point"]
    risk_level = row["Risk_Level"]

    if point == "Torque + Tool Wear":
        return "Critical"

    if risk_level == "Critical":
        return "Critical"

    if point in [
        "High Torque",
        "High Tool Wear",
        "High Air Temp + Low Temp Diff",
        "RPM + Torque"
    ]:
        return "High"

    if point in [
        "Temperature Condition",
        "High RPM",
        "Power Condition",
        "Load / Wear",
        "Tool Wear"
    ]:
        return "Medium"

    return "Low"


risk_df["Improvement_Priority"] = (
    risk_df.apply(
        get_improvement_priority,
        axis=1
    )
)


# ============================================================
# 40-9. Improvement Point Summary
# ============================================================

print("\n[Improvement Point Summary]")

improvement_summary = (
    risk_df
    .groupby(
        [
            "Improvement_Failure_Type",
            "Improvement_Point",
            "Improvement_Priority"
        ],
        dropna=False
    )
    .agg(
        Machines=(
            "UDI",
            "count"
        ),
        Actual_Failures=(
            "Machine failure",
            "sum"
        ),
        Avg_Risk_Score=(
            "Risk_Score",
            "mean"
        )
    )
    .sort_values(
        [
            "Improvement_Priority",
            "Actual_Failures"
        ],
        ascending=[True, False]
    )
)

print(
    improvement_summary
    .to_string()
)


# ============================================================
# 40-10. Critical Improvement Target
# ============================================================

print("\n" + "=" * 60)
print("40-10. Critical Improvement Target")
print("=" * 60)

critical_improvement = (
    risk_df[
        risk_df["Improvement_Point"]
        == "Torque + Tool Wear"
    ]
)

print(
    "Target Machines :",
    len(critical_improvement)
)

print(
    "Actual Failures :",
    critical_improvement[
        "Machine failure"
    ].sum()
)

print(
    "Average Risk    :",
    critical_improvement[
        "Risk_Score"
    ].mean()
)

print(
    "\n[Critical Target Preview]"
)

print(
    critical_improvement[
        [
            "UDI",
            "Product ID",
            "Type",
            "Torque [Nm]",
            "Tool wear [min]",
            "Risk_Score",
            "Predicted_Failure_Type",
            "Improvement_Point",
            "Control_Action",
            "Improvement_Priority"
        ]
    ]
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .head(20)
    .to_string(index=False)
)


# ============================================================
# 41. Final Pipeline Summary
# ============================================================

print("\n" + "=" * 60)
print("41. Final Pipeline Summary")
print("=" * 60)

print(
    """
[Pipeline]

Raw Data
    ↓
Data Quality Check
    ↓
EDA
    ↓
Machine Failure Analysis
    ↓
Failure Type Analysis
    ↓
Statistical Significance Test
    ↓
Interaction / Risk Zone Analysis
    ↓
Feature Engineering
    ↓
Machine Failure Prediction
    ↓
Failure Type Prediction
    ↓
SHAP Interpretation
    ↓
Risk Score
    ↓
Risk Level
    ↓
Failure Type Risk
    ↓
Key Risk Factor
    ↓
Improvement Point
    ↓
Control Action
    ↓
Final CSV
"""
)

print(
    "Core Story:"
)

print(
    "설비 고장 여부를 예측하는 데서 끝나지 않고,"
)

print(
    "고장 위험도가 높은 설비를 식별한 후"
)

print(
    "Failure Type + SHAP + Interaction 분석을 통해"
)

print(
    "어떤 공정 조건을 개선해야 하는지까지 연결."
)

print(
    "\nKey Improvement Story:"
)

print(
    "OSF → Torque + Tool Wear "
    "→ Critical Risk "
    "→ Torque 및 Tool Wear 동시 모니터링"
)


# ============================================================
# 42. Final Output
# ============================================================

print("\n" + "=" * 60)
print("42. Final Output")
print("=" * 60)


# 최종 결과에 사용할 컬럼
final_cols = [
    "UDI",
    "Product ID",
    "Type",

    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",

    "Machine failure",

    "Failure_Probability",
    "Risk_Score",
    "Risk_Level",

    "Predicted_Failure_Type",
    "Max_Failure_Type_Probability",

    "TWF_Probability",
    "HDF_Probability",
    "PWF_Probability",
    "OSF_Probability",

    "Key_Risk_Factor",
    "Recommended_Action",

    "Improvement_Failure_Type",
    "Improvement_Point",
    "Improvement_Goal",
    "Control_Action",
    "Improvement_Priority"
]


# 존재하는 컬럼만 선택
final_cols = [
    col
    for col in final_cols
    if col in risk_df.columns
]

final_df = risk_df[
    final_cols
].copy()


# ----------------------------
# Final CSV Save
# ----------------------------

final_output_path = (
    BASE_DIR
    / "predictive_maintenance_final.csv"
)

final_df.to_csv(
    final_output_path,
    index=False,
    encoding="utf-8-sig"
)


# ----------------------------
# Final Result
# ----------------------------

print(
    "\nFinal Dataset Shape :",
    final_df.shape
)

print(
    "Saved Path :",
    final_output_path
)


# ----------------------------
# Final Risk Level
# ----------------------------

print("\n[Risk Level]")

print(
    final_df[
        "Risk_Level"
    ]
    .value_counts()
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],
        fill_value=0
    )
)


# ----------------------------
# Final Failure Type
# ----------------------------

print("\n[Predicted Failure Type]")

print(
    final_df[
        "Predicted_Failure_Type"
    ]
    .value_counts()
)


# ----------------------------
# Final Improvement Priority
# ----------------------------

print("\n[Improvement Priority]")

print(
    final_df[
        "Improvement_Priority"
    ]
    .value_counts()
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],
        fill_value=0
    )
)


# ----------------------------
# Final Dataset Preview
# ----------------------------

print("\n[Final Dataset Preview]")

preview_cols = [
    "UDI",
    "Product ID",
    "Type",
    "Risk_Score",
    "Risk_Level",
    "Predicted_Failure_Type",
    "Key_Risk_Factor",
    "Improvement_Point",
    "Improvement_Priority"
]

print(
    final_df[
        preview_cols
    ]
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .head(20)
    .to_string(index=False)
)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 60)
print("Pipeline Completed Successfully")
print("=" * 60)

print(
    "\nFinal CSV:"
)

print(
    final_output_path
)