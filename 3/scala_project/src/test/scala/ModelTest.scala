import breeze.linalg.{DenseMatrix, convert}
import org.scalactic.Tolerance.convertNumericToPlusOrMinusWrapper
import org.scalatest.funsuite.AnyFunSuite

import java.io.File
import java.nio.file.Files

class ModelTest extends AnyFunSuite {

  test("Model.shift") {
    val X = convert(DenseMatrix(
      (2, 3, 4),
      (3, 2, 1),
      (3, 5, 6),
      (2, 1, 2),
      (2, 4, 3),
    ), Double)
    val shiftedX = convert(DenseMatrix(
      (1, 2, 3, 4),
      (1, 3, 2, 1),
      (1, 3, 5, 6),
      (1, 2, 1, 2),
      (1, 2, 4, 3),
    ), Double)

    Model.shiftX(X).toArray.lazyZip(shiftedX.toArray).map((x1, x2) => assert(x1 === x2 +- 1e-6))
  }

  test("Model.fileWork") {
    val matrix = convert(DenseMatrix(
      (2, 3, 4),
      (3, 2, 1),
    ), Double)

    val file = Files.createTempFile("test", ".csv")
    Model.saveMatrixToCsv(file.toString, matrix)
    val loadedMatrix = Model.loadMatrixFromCsv(file.toString)
    new File(file.toString).delete()

    matrix.toArray.lazyZip(loadedMatrix.toArray).map((x1, x2) => assert(x1 === x2 +- 1e-6))
  }

  test("Model.integration") {
    val fileXTrain = Files.createTempFile("test_x_train", ".csv").toString
    val fileXTest = Files.createTempFile("test_x_test", ".csv").toString
    val fileTargets = Files.createTempFile("test_targets", ".csv").toString
    val filePredict = Files.createTempFile("test_predict", ".csv").toString
    val fileModel = Files.createTempFile("test_model", ".csv").toString

    val X = convert(DenseMatrix(
      (2, 3, 4),
      (3, 2, 1),
      (3, 5, 6),
      (2, 1, 2),
      (2, 4, 3),
    ), Double)
    val y = convert(DenseMatrix(
      (7, 2),
      (5, 3),
      (6, 1),
      (5, 4),
      (3, 2),
    ), Double)
    Model.saveMatrixToCsv(fileXTrain, X)
    Model.saveMatrixToCsv(fileTargets, y)

    Model.fit(fileXTrain, fileTargets, fileModel)

    val W = DenseMatrix(
      (3.015625, 4.78125),
      (0.9375, -0.125),
      (-1.171875, -0.59375),
      (1.078125, -0.09375),
    )
    val resW = Model.loadMatrixFromCsv(fileModel)
    resW.toArray.lazyZip(W.toArray).map((x, w) => assert(x === w +- 1e-6))

    val X_test = convert(DenseMatrix(
      (3, 5, 6),
      (3, 2, 8)
    ), Double)
    Model.saveMatrixToCsv(fileXTest, X_test)
    val y_test = DenseMatrix(
      (6.4375, 0.875),
      (12.109375, 2.46875)
    )
    Model.predict(fileModel, fileXTest, filePredict)

    val predicted = Model.loadMatrixFromCsv(filePredict)

    predicted.toArray.lazyZip(y_test.toArray).map(
      (yp, yt) => assert(yt === yp +- 1e-6)
    )

    new File(fileXTrain).delete()
    new File(fileXTest).delete()
    new File(fileTargets).delete()
    new File(filePredict).delete()
    new File(fileModel).delete()
  }
}