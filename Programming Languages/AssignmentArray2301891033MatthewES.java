
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
public class AssignmentArray2301891033MatthewES {

    /**
     * @param args the command line arguments
     */
    static Scanner scan = new Scanner(System.in);
    
    public static void printArray(int array[]){
        for (int i : array){
            System.out.println(i);
        }
    }
    
    public static boolean doesArrayContain(int array[], int element){
        for (int i : array){
            if (i == element){
                return true;
            }
        }
        return false;
    }
    
    public static void askUserForTenIntegersAndPrint(){
        int arr[] = new int[10];
        for (int i = 0; i < 10; i++){
            System.out.print("Input integer " + (i+1) + " : ");
            int inputNumber = scan.nextInt();
            arr[i] = inputNumber;
        }
        printArray(arr);
    } 
    
    public static void askTenIntegersAndAskForANumberToCheck(){
        int arr[] = new int[10];
        for (int i = 0; i < 10; i++){
            System.out.print("Input integer " + (i+1) + " : ");
            int inputNumber = scan.nextInt();
            arr[i] = inputNumber;
        }
        
        System.out.print("Input integer to check: ");
        int numberToCheck = scan.nextInt();
        
        boolean isExist = doesArrayContain(arr, numberToCheck);
        if (isExist)
            System.out.println("The number exists in the array.");
        else
            System.out.println("The number doesn't exist in the array.");
    } 
    
    public static void askUserForTwentyIntegersAndPrintTheSummary(){
        int positiveNumber = 0, negativeNumber = 0, oddNumber = 0, evenNumber = 0, zeroNumber = 0;
        for (int i = 0; i < 20; i++){
            System.out.print("Input integer " + (i+1) + " : ");
            int inputNumber = scan.nextInt();
            if (inputNumber > 0)
                positiveNumber++;
            else if (inputNumber < 0)
                negativeNumber++;
            else if (inputNumber == 0)
                zeroNumber++;
            if (inputNumber % 2 == 0)
                evenNumber++;
            else
                oddNumber++;
        }
        System.out.println("Positive: " + positiveNumber);
        System.out.println("Negative: " + negativeNumber);
        System.out.println("Zero: " + zeroNumber);
        System.out.println("Odd: " + oddNumber);
        System.out.println("Even: " + evenNumber);
    } 
    
    public static int sumOfArray(int array[]){
        int sum = 0;
        for (int i : array)
            sum += i;
        return sum;
    }
    
    public static void isPalindrome(int array[], int size){
        int j = size - 1;
        boolean isPalindrome = true;
        for (int i = 0; i < size/2; i++){
            if (array[i] != array[j]){
                isPalindrome = false;
                break;
            }
            j--;
        }
        if (isPalindrome)
            System.out.println("It is palindrome!");
        else
            System.out.println("It is not a palindrome!");
    }
    
    public static void splitArray (int array[], int size){
        int array1[] = new int[size/2];
        int array2[] = new int[size/2];
        
        for (int i = 0; i < size/2; i++){
            array1[i] = array[i];
        }
        
        int j = 0;
        
        for (int i = size/2; i < size; i++){
            array2[j] = array[i];
            j++;
        }
        
        System.out.println("ARRAY 1");
        printArray(array1);
        
        System.out.println("ARRAY 2");
        printArray(array2);
    }
    
    public static int[] splitHighestValueInArray(int[] array, int size){
        int maxValueIndex = 0;
        int maxValue = 0;
        int secondMaxValue = 0;
        
        for (int i = 0; i < size; i++){
            if (array[i] > maxValue){
                maxValue = array[i];
                maxValueIndex = i;
            }
        }
        
        for (int i = 0; i < size; i++){
            if (array[i] != maxValue && array[i] > secondMaxValue){
                secondMaxValue = array[i];
            }
        }
        
        int attributiveValue = maxValue - secondMaxValue;
        
        int newArray[] = new int[size+1];
        
        int j = 0;
        
        for (int i = 0; i < size+1; i++){
            if (j == maxValueIndex){
                newArray[i] = secondMaxValue;
                i++;
                newArray[i] = attributiveValue;
            }
            else
                newArray[i] = array[j];
            j++;
        }
        
        return newArray;
    }
    
    public static int[] shiftRightArray(int[] array, int size){
        
        for (int i = size-1; i >= 1; i--){
            int temp = array[i];
            array[i] = array[i-1];
            array[i-1] = temp;
        }
        
        return array;
    }
    
    public static int[] sortAscending(int[] array, int size){
        
        // BUBBLE SORT
        int i, j;  
        for (i = 0; i < size-1; i++){
            for (j = 0; j < size-i-1; j++)  
                if (array[j] > array[j+1]){
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
        }
        
        return array;
    }
            
    public static int findMax(int[] array){
        int maxValue = 0;
        for (int i : array){
            if (array[i] > maxValue){
                maxValue = array[i];
            }
        }
        return maxValue;
    }
    
    public static int findMin(int[] array){
        int minValue = 0;
        for (int i : array){
            if (array[i] < minValue){
                minValue = array[i];
            }
        }
        return minValue;
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        // 1
        askUserForTenIntegersAndPrint();
        
        // 2
        askTenIntegersAndAskForANumberToCheck();
        
        // 3
        askUserForTwentyIntegersAndPrintTheSummary();
        
        int randomIntArray[] = new int[]{1, 4, 5, 6, 7, 8, 9, 0, 3, 2};
        int randomIntArray2[] = new int[]{1, 4, 5, 6, 7, 7, 6, 5, 4, 1};
        
        // 4
        int sum = sumOfArray(randomIntArray);
        System.out.println("The sum of array 1 4 5 6 7 8 9 0 3 2 " + " = " + sum);
        
        // 5
        int max = findMax(randomIntArray);
        int min = findMin(randomIntArray);
        System.out.println("Find max and min of 1 4 5 6 7 8 9 0 3 2");
        System.out.println("MAX: "+ Integer.toString(max) + ", MIN: " + Integer.toString(min));
        
        // 6
        System.out.println("Check if 1 4 5 6 7 7 6 5 4 1 is a palindrome.");
        isPalindrome(randomIntArray2, randomIntArray2.length);
        
        // 7
        splitArray(randomIntArray, randomIntArray.length);
        
        // 8
        System.out.println("SPLIT HIGHEST VALUE OF {1 4 5 6 7 8 9 0 3 2}");
        int maxSplitArray[] = splitHighestValueInArray(randomIntArray, randomIntArray.length);
        printArray(maxSplitArray);
        
        // 9
        System.out.println("SHIFTED CIRCULARLY RIGHT OF {1 4 5 6 7 8 9 0 3 2}");
        int shiftedRightArray[] = shiftRightArray(randomIntArray, randomIntArray.length);
        printArray(shiftedRightArray);
        
        // 10
        System.out.println("ASCENDING ORDER OF {1 4 5 6 7 8 9 0 3 2}");
        int ascendingArray[] = sortAscending(randomIntArray, randomIntArray.length);
        printArray(ascendingArray);
        
    }
    
}
