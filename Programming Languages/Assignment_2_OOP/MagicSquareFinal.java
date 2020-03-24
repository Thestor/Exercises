import java.util.ArrayList;
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
public class MagicSquareFinal {

    private int[][] magicSquare;
    private int size;
    
    // Generate a magic square using the siamese method.
    private void createMagicSquareSiamese(){
        
        // The iterator, I guess?
        int row = 0;
        int col = this.size/2;
        
        // Place '1' in the middle of the uppermost row.
        this.magicSquare[row][col] = 1;

        // Begin placing 2 to size*size one by one over all empty units.
        for (int i = 2; i <= this.size*this.size; i++) {
            
            // Incrementally place subsequent numbers in the square one unit above the previously iterated square and to the right.
            if (this.magicSquare[(row - 1 + this.size) % this.size][(col + 1) % this.size] == 0) {
                row = (row - 1 + this.size) % this.size;
                col = (col + 1) % this.size;
            }
            
            // If a filled square is encountered, instead fill the square below the previously iterated square.
            else {
                row = (row + 1) % this.size;
            }
            
            // Place the subsequent number in the current position of the iterator.
            this.magicSquare[row][col] = i;
        }
    }
    
    // Generate a magic square which is doubly-even-sized.
    private void createMagicSquareDoublyEven(){
        
        // Define the iterator.
        int row = 0;
        int col = 0;
        
        // Split the grid into 4x4 subsquares and cross out the subsquares. Place subsequent numbers ascendingly.
        for (int i = 1; i <= this.size*this.size; i++){
            
            // If it's placed in a crossed-out square, then place (size*size+1) - i number.
            if ((row % 4 == 0 || row % 4 == 3) && (col % 4 == 0 || col % 4 == 3)){
                this.magicSquare[row][col] = ((this.size*this.size+1) - i);
            }
            else if ((row % 4 == 1 || row % 4 == 2) && (col % 4 == 1 || col % 4 == 2)){
                this.magicSquare[row][col] = ((this.size*this.size+1) - i);
            }
            
            // Otherwise, place i.
            else{
                this.magicSquare[row][col] = i;
            }
            
            // Continue iteration.
            if (col == this.size-1){
                col = 0;
                row++;
            }
            else
                col++;
        }
    }
    
    // Generate a magic square for n = 4m+2.
    private void createMagicSquareSinglyEven(){
        
        // Determine how many L, U, and X exist. Note that there is only one U row.
        
        int Lsquares = ((this.size-2) / 4) + 1;
        int Xsquares = ((this.size-2) / 4) - 1;
        
        int halfSize = this.size/2-1;
        
        // Find the index of uppermost left subsquare of small squares.
        ArrayList<int[]> Lindexes = new ArrayList<>();
        ArrayList<int[]> Uindexes = new ArrayList<>();
        ArrayList<int[]> Xindexes = new ArrayList<>();

        // Generate the indexes of L squares.
        for (int irow = 0; irow < Lsquares*2; irow += 2){
            for (int icol = 0; icol < this.size; icol += 2){
                if (irow == (Lsquares*2)-2 && icol == halfSize){
                    int[] temp = {irow, icol};
                    Uindexes.add(temp);
                }
                else{
                    int[] temp = {irow, icol};
                    Lindexes.add(temp);
                }
            }
        }
        
        // Generate the indexes of U squares.
        for (int irow = Lsquares * 2; irow < Lsquares * 2 + 2; irow += 2){
            for (int icol = 0; icol < this.size; icol += 2){
                if (irow == Lsquares * 2 && icol == halfSize){
                    int[] temp = {irow, icol};
                    Lindexes.add(temp);
                }
                else{
                    int[] temp = {irow, icol};
                    Uindexes.add(temp);
                }
            }
        }
        
        // Generate the indexes of X squares.
        for (int irow = Lsquares * 2 + 2; irow < Lsquares * 2 + 2 + Xsquares*2; irow += 2){
            for (int icol = 0; icol < this.size; icol += 2){
                int[] temp = {irow, icol};
                Xindexes.add(temp);
            }
        }
     
        // Define the iterator.
        int row = 0;
        int col = halfSize;
        
        // Begin placing 1 to size*size one by one over all empty units, according to the letters.
        for (int i = 1; i <= this.size*this.size; i += 4) {
            
            // Check which letter the index belongs to.
            int[] tempRowCol = {row, col};
            
            // Is it in the L index?
            if (Lindexes.stream().anyMatch(a -> Arrays.equals(a, tempRowCol))){
                this.magicSquare[row][col+1] = i;
                this.magicSquare[row+1][col] = i+1;
                this.magicSquare[row+1][col+1] = i+2;
                this.magicSquare[row][col] = i+3;
            }
            
            // Is it in the U index?
            else if (Uindexes.stream().anyMatch(a -> Arrays.equals(a, tempRowCol))){
                this.magicSquare[row][col] = i;
                this.magicSquare[row+1][col] = i+1;
                this.magicSquare[row+1][col+1] = i+2;
                this.magicSquare[row][col+1] = i+3;
            }
            
            // Is it in the X index?
            else if (Xindexes.stream().anyMatch(a -> Arrays.equals(a, tempRowCol))){
                this.magicSquare[row][col] = i;
                this.magicSquare[row+1][col+1] = i+1;
                this.magicSquare[row+1][col] = i+2;
                this.magicSquare[row][col+1] = i+3;
            }
            
            // It shouldn't go here, but what if it goes here? Throw an error.
            else
                throw new RuntimeException("ERROR WHILE FINDING INDEX");
            
            // Incrementally place subsequent numbers in the 2x2 square one unit above the previously iterated square and to the right.
            if (this.magicSquare[(row - 2 + this.size) % this.size][(col + 2) % this.size] == 0) {
                row = (row - 2 + this.size) % this.size;
                col = (col + 2) % this.size;
            }
            
            // If a filled square is encountered, instead fill the square below the previously iterated square.
            else {
                row = (row + 2) % this.size;
            }
        }
    }
    
    // Construct and decide which method to use.
    public MagicSquareFinal (int size) { 
        
        this.size = size;
        this.magicSquare = new int[size][size];
        
        // Siamese method only allows odd-sized squares.
        if (size % 2 == 0 && (size / 2) % 2 == 0){
            this.createMagicSquareDoublyEven();
        }
        else if (size % 2 == 0 && (size / 2) % 2 != 0){
            this.createMagicSquareSinglyEven();
        }
        else{
            this.createMagicSquareSiamese();
        }
    }

    // Print the square.
    public void printMagicSquare(){
        for (int i = 0; i < this.size; i++) {
            for (int j = 0; j < this.size; j++) {
                
                // Just to tidy things up.
                if (this.magicSquare[i][j] < 10)  System.out.print(" ");
                if (this.magicSquare[i][j] < 100) System.out.print(" ");
                
                System.out.print(this.magicSquare[i][j] + " ");
            }
            System.out.println();
        }
    }
}

