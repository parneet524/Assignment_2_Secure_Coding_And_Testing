import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.Scanner;

public class App {

    public static void saveToDatabase(String name) {
        String url = System.getenv().getOrDefault("DB_URL", "jdbc:mysql://localhost/testdb");
        String user = System.getenv().getOrDefault("DB_USER", "admin");
        String password = System.getenv().getOrDefault("DB_PASSWORD", "");

        String query = "INSERT INTO users (name) VALUES (?)";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setString(1, name);
            stmt.executeUpdate();
            System.out.println("User saved successfully.");

        } catch (Exception e) {
            System.out.println("Database error.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine().trim();

        if (!name.isEmpty()) {
            saveToDatabase(name);
        } else {
            System.out.println("No name entered.");
        }

        scanner.close();
    }
}
