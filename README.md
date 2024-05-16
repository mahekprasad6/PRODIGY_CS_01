Task-01

Implement Caesar Cipher

Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. 

Here is an example of how to use the Caesar cipher to encrypt the message “HELLO” with a shift of 3:
Write down the plaintext message: HELLO
Choose a shift value. In this case, we will use a shift of 3.
Replace each letter in the plaintext message with the letter that is three positions to the right in the alphabet.
         H becomes K (shift 3 from H)

         E becomes H (shift 3 from E)

         L becomes O (shift 3 from L)

         L becomes O (shift 3 from L)

         O becomes R (shift 3 from O)

      4.The encrypted message is now “KHOOR”.

To decrypt the message, you simply need to shift each letter back by the same number of positions. In this case, you would shift each letter in “KHOOR” back by 3 positions to get the original message, “HELLO”.
