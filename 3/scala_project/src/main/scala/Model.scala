import breeze.linalg.{DenseMatrix, csvread, csvwrite, inv}

import java.io.File

object Model {
  def fit(X: DenseMatrix[Double], y: DenseMatrix[Double]): DenseMatrix[Double] = {
    val shiftedX = shiftX(X)
    (inv(shiftedX.t * shiftedX) * shiftedX.t) * y
  }

  def fit(fileX: String, fileTargets: String, fileModel: String): Unit
  = saveMatrixToCsv(fileModel, fit(loadMatrixFromCsv(fileX), loadMatrixFromCsv(fileTargets)))

  def predict(W: DenseMatrix[Double], X: DenseMatrix[Double]): DenseMatrix[Double] = {
    val shiftedX = shiftX(X)
    shiftedX * W
  }

  def predict(fileModel: String, fileTestX: String, filePredict: String): Unit
  = saveMatrixToCsv(filePredict, predict(loadMatrixFromCsv(fileModel), loadMatrixFromCsv(fileTestX)))

  def shiftX(X: DenseMatrix[Double]): DenseMatrix[Double]
  = DenseMatrix.horzcat(DenseMatrix.ones[Double](X.rows, 1), X)

  def loadMatrixFromCsv(fileName: String): DenseMatrix[Double]
  = csvread(new File(fileName))

  def saveMatrixToCsv(fileName: String, matrix: DenseMatrix[Double]): Unit
  = csvwrite(new File(fileName), matrix)
}
