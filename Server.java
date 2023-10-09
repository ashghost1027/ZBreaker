package WebServerTrial;

import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;
import java.util.ArrayList;

public class Server {

    static ArrayList<String> userIPs = new ArrayList<>();

    public static void addUser(String userIP) {
        userIPs.add(userIP);
    }

    public static void main(String[] args) {
        try {

            try (ServerSocket serverSocket = new ServerSocket(6969)) {
                while (true) {
                    Socket client = serverSocket.accept();
                    InputStreamReader input = new InputStreamReader(client.getInputStream());
                    BufferedReader buffer = new BufferedReader(input);
                    // Read the 1st Request from the client
                    StringBuilder request = new StringBuilder();
                    String line = buffer.readLine();
                    while (line != null && !line.isBlank()) {

                        request.append(line+"\n");
                        line = buffer.readLine();
                    }
                    String[] userProperties = request.toString().split(", ");
                    Server.addUser(userProperties[1]);
                    System.out.println(request);
                    BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));
                    switch(userProperties[0]){
                        case "Linux": writer.write("Hello Linux User");writer.flush();writer.close();System.out.println("hello");
                        break;
                        case "MacOS": writer.write("Hello Mac user"); writer.flush(); writer.close();
                        break;
                        case "Windows": writer.write("Hello Windows user"); writer.flush();writer.close();
                    }
                    client.close();
                }

            }

        } catch (Exception e) {
            System.out.println(e.getLocalizedMessage());
        }
    }
}
