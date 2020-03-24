
import java.util.Arrays;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Matthew
 */
public class Driver {

    /**
     * @param args the command line arguments
     */
    
    static Scanner scan = new Scanner(System.in);
    
    public static void main(String[] args) {
        
        int[] randomArray = {4, 8, 6, 2, 5, 3};
        
        // Question 1
        System.out.println("Splitting {4, 8, 6, 2, 5, 3}");
        
        int[] splitArray = Utility.splitHighestValueInArray(randomArray, randomArray.length);
        System.out.println(Arrays.toString(splitArray));
        
        System.out.println("--------------------");
        
        // Question 2
        System.out.println("Rotating {4, 8, 6, 2, 5, 3}");
        System.out.print("How many rotations? ");
        
        int rotationTimes = scan.nextInt();
        
        int[] rotatedArray = Utility.shiftRightArray(randomArray, randomArray.length, rotationTimes);
        System.out.println(Arrays.toString(rotatedArray));
        
        System.out.println("--------------------");
        
        // Question 3
        int[][] randomMatrix = {{1, 3, 5}, {3, 6, 7}, {5, 7, 1}};
        int[][] randomMatrix2 = {{1, 3, 4}, {3, 9, 7}, {5, 2, 1}};
        
        boolean randomMatrixSymmetric = Utility.isMatrixSymmetric(randomMatrix, randomMatrix.length);
        boolean randomMatrix2Symmetric = Utility.isMatrixSymmetric(randomMatrix2, randomMatrix2.length);
        
        System.out.println("Matrix 1 - {1, 3, 5}, {3, 6, 7}, {5, 7, 1} is symmetric => " + randomMatrixSymmetric);
        System.out.println("Matrix 2 - {1, 3, 4}, {3, 9, 7}, {5, 2, 1} is symmetric => " + randomMatrix2Symmetric);
        
        System.out.println("--------------------");
        
        // Question 4
        System.out.println("Magic Square Testing");
        System.out.print("Input the size? ");
        
        int squareSize = scan.nextInt();
        
        MagicSquareFinal x = Utility.createNewMagicSquare(squareSize);
        x.printMagicSquare();
        
    }
    
}
