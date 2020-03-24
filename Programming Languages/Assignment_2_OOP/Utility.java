/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Matthew
 */

public class Utility {
    
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
    
    public static int[] shiftRightArray(int[] array, int size, int times){
        
        for (int j = 0; j < times; j++){
            for (int i = size-1; i >= 1; i--){
                int temp = array[i];
                array[i] = array[i-1];
                array[i-1] = temp;
            }
        }
        
        return array;
    } 
    
    public static boolean isMatrixSymmetric(int matrix[][], int size){ 
        for (int i = 0; i < size; i++) 
            for (int j = 0; j < size; j++) 
                if (matrix[i][j] != matrix[j][i]) 
                    return false; 
        return true; 
    }  
    
    public static MagicSquareFinal createNewMagicSquare(int size){
        MagicSquareFinal x = new MagicSquareFinal(size);
        return x;
    }
}
