import breeze.linalg.{DenseMatrix, inv}

object Model {
  def fit(X: DenseMatrix[Double], y: DenseMatrix[Double]): DenseMatrix[Double] = {
    val shiftedX = shiftX(X)
    (inv(shiftedX.t * shiftedX) * shiftedX.t) * y
  }

  def predict(W: DenseMatrix[Double], X: DenseMatrix[Double]): DenseMatrix[Double] = {
    val shiftedX = shiftX(X)
    shiftedX * W
  }

  def shiftX(X: DenseMatrix[Double]): DenseMatrix[Double]
  = DenseMatrix.horzcat(DenseMatrix.ones[Double](X.rows, 1), X)
}
