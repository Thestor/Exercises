
import java.util.Arrays;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Matthew
 */
public class reverseArray {
    
    public static void reverse(String arr[], int size){
        int j = size - 1;
        for (int i = 0; i < size/2; i++){
            String temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            j--;
        }
    } 
    public static void main(String[] args) {
        String x[] = {"aaa", "bbb", "ccc", "ddd", "eee"};
        int sizeOfArray = x.length;
        System.out.println(Arrays.toString(x));
        reverse(x, sizeOfArray);
        System.out.println(Arrays.toString(x));
    }        
    
}
//