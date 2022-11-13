import breeze.linalg.{*, DenseMatrix, convert, zipValues}
import org.scalactic.Tolerance.convertNumericToPlusOrMinusWrapper
import org.scalatest.funsuite.AnyFunSuite

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
  test("Model.fit_predict") {
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
    val W = DenseMatrix(
      (3.015625, 4.78125),
      (0.9375, -0.125),
      (-1.171875, -0.59375),
      (1.078125, -0.09375),
    )
    val resW = Model.fit(X, y)
    resW.toArray.lazyZip(W.toArray).map((x, w) => assert(x === w +- 1e-6))

    val x_test = convert(DenseMatrix(
      (3, 5, 6),
      (3, 2, 8)
    ), Double)
    val y_test = DenseMatrix(
      (6.4375, 0.875),
      (12.109375, 2.46875)
    )
    Model.predict(resW, x_test).toArray.lazyZip(y_test.toArray).map(
      (yp, yt) => assert(yt === yp +- 1e-6)
    )
  }
}