import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.util.Scanner;

public class App {

    public static void saveToDatabase(String name) {

        // Hardcoded credentials (Security issue)
        String url = "jdbc:mysql://localhost/testdb";
        String user = "admin";
        String password = "admin123";

        // SQL Injection vulnerability
        String query = "SELECT * FROM users WHERE name = '" + name + "'";

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();
            stmt.executeQuery(query);

            System.out.println("Query executed successfully.");

        } catch (Exception e) {
            System.out.println("Database error.");
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        saveToDatabase(name);

        scanner.close();
    }
}
