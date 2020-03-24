/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Matthew
 */
public class MagicSquare {

    private int[][] magicSquare;
    private int size;
    
    // Generate a magic square using the siamese method.
    public MagicSquare (int size) { 
        
        // Siamese method only allows odd-sized squares.
        if (size % 2 == 0){
            System.out.println("Error: Size must be odd (using Siamese method)");
            System.exit(0);
        }

        this.size = size;
        this.magicSquare = new int[size][size];

        // The iterator, I guess?
        int row = 0;
        int col = size/2;
        
        // Place '1' in the middle of the uppermost row.
        this.magicSquare[row][col] = 1;

        // Begin placing 2 to size*size one by one over all empty units.
        for (int i = 2; i <= size*size; i++) {
            
            // Incrementally place subsequent numbers in the square one unit above the previously iterated square and to the right.
            if (this.magicSquare[(row - 1 + size) % size][(col + 1) % size] == 0) {
                row = (row - 1 + size) % size;
                col = (col + 1) % size;
            }
            
            // If a filled square is encountered, instead fill the square below the previously iterated square.
            else {
                row = (row + 1) % size;
            }
            
            // Place the subsequent number in the current position of the iterator.
            this.magicSquare[row][col] = i;
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
