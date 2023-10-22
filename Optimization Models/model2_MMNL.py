import numpy as np
import pandas as pd
import pylogit as pl

# Generate dummy data
np.random.seed(0)
num_obs = 1000
data = pd.DataFrame({
    'obs_id_column': np.repeat(np.arange(num_obs), 2),
    'alternative_id': np.tile([1, 2], num_obs),
    'choice_column': np.random.choice([0, 1], 2 * num_obs),
    'some_feature_1': np.random.randn(2 * num_obs),
    'some_feature_2': np.random.randn(2 * num_obs)
})

# Ensure at least one alternative is chosen for each observation
data.loc[data.groupby('obs_id_column').choice_column.transform(sum) == 0, 'choice_column'] = 1

# Create choice model specification
specification = {
    "variable_1": ["some_feature_1", "some_feature_2"],
}
labels = {
    "variable_1": "Variable 1 Label",
}

# Mixed Logit Model
mixed_logit = pl.create_choice_model(
    data,
    alt_id_col="alternative_id",
    obs_id_col="obs_id_column",
    choice_col="choice_column",
    specification=specification,
    model_type="Mixed Logit",
    names=labels,
    mixing_id_col="obs_id_column",
    mixing_vars=["variable_1"],
)

# Specify the initial values and bounds
init_vals = np.zeros(4)
lower_bounds = [-np.inf, -np.inf, 0.001, 0.001]
upper_bounds = [np.inf, np.inf, np.inf, np.inf]

# Fit the model
mixed_logit.fit_mle(init_vals, lower_bounds=lower_bounds, upper_bounds=upper_bounds)

# Print model results
print(mixed_logit.get_statsmodels_summary())
