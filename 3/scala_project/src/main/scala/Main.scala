object Main {
  def main(args: Array[String]): Unit = {
    if (args.length != 5) {
      println("Enter next arguments: trainFilename, testFilename, targetsFilename, predictFilename, modelFilename")
      return
    }
    val List(trainFilename, testFilename, targetsFilename, predictFilename, modelFilename) = args.toList

    Model.fit(trainFilename, targetsFilename, modelFilename)
    Model.predict(modelFilename, testFilename, predictFilename)
  }
}