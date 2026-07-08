// with coverting the int to string and checking if the string is equal to its reverse

// public class Palindrome_Numbers_java {

//     public static boolean isPalindrome(int x) {
//         String word = String.valueOf(x);
//         String reverse_word = "";

//         for ( int i = word.length() - 1; i >= 0; i--) {
//             reverse_word += word.charAt(i);
//         }
//         if (word.equals(reverse_word)) {
//             return true;
//         } else {
//             return false;
//         }
//     }
//     public static void main(String[] args) {
//         System.out.println(isPalindrome(121));
//         System.out.println(isPalindrome(-121));
//         System.out.println(isPalindrome(10));
//     }
// }

// Without converting the int to string and checking if the number is equal to its reverse

public class Palindrome_Numbers_java {

    public static boolean isPalindrome(int x) {
        int original = x;
        int reverse = 0;

        while (x > 0) {
            int digit = x % 10;
            reverse = reverse * 10 + digit;
            x = x / 10;
        }

        return original == reverse;

    }
    public static void main(String[] args) {
        System.out.println(isPalindrome(121));
        System.out.println(isPalindrome(-121));
        System.out.println(isPalindrome(10));
    }
}
