"L1: Lasso Regression vs L2: Ridge Regression"
"L2 adds lambda*((coefficient)**2) to loss function >< L1 adds lambda*(abs(coefficient)) to loss function"
"L2 tries to estimate the mean of data to avoid overfitting >< L1 tries to estimate teh median of data"
"L1 will shrink less important feature's coefficient to 0 => create sparse vectors of weights like (0, 1, 0, 1, 1, 0)" \
    "=> works well for feature selection when dataset is large"
"L2 will create sparsity of weights like (0.5, 0.3, -0.2, 0.4, 0.1) => L2 will go towards 0 but never = 0"
""
