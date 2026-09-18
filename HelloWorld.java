public class HelloWorld {
    public static void main(String[] args) {
        System.out.println(greet("World"));
    }

    static String greet(String name) {
        return "Hello, " + name + "!";
    }
}