import scala.io.Source
import scala.collection.mutable.ListBuffer

object Day01 extends App {
  var elves = new ListBuffer[Int]
  var tmp_sum = 0
  for (line <- Source.fromResource("01.txt").getLines) {
    if (line.isEmpty){
      elves += tmp_sum
      tmp_sum = 0
    }
    else {
      tmp_sum += line.toInt
    }
  }  
  println("Answer #1: " + elves.max)
  println("Answer #2: " + elves.sorted.takeRight(3).sum)
}
