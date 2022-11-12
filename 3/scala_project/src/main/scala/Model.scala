import breeze.linalg.{DenseMatrix, inv}

object Model {
  def fit(X: DenseMatrix[Double], y: DenseMatrix[Double]): DenseMatrix[Double]
  = (inv(X.t * X) * X.t) * y

  def predict(W: DenseMatrix[Double], X: DenseMatrix[Double]): DenseMatrix[Double]
  = X * W
}
