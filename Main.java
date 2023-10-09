package WebServerTrial;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {
    public void returnHelloWorld(Socket client) throws IOException {
        OutputStream clientOutput = client.getOutputStream();
        String response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello World!!";
        clientOutput.write(response.getBytes());
        clientOutput.flush();
        client.close();
    }

    public void images(Socket client, String path) throws IOException {
        FileInputStream files = new FileInputStream(path);
        OutputStream clientReq = client.getOutputStream();
        byte[] filed = files.readAllBytes();
        files.close();

        String respond = "HTTP/1.1 200 OK\r\nContent-Length:" + filed.length + "\r\n\r\n";
        clientReq.write(respond.getBytes());
        clientReq.write(filed);
        clientReq.flush();
        // client.close();
    }

    public void noInput(Socket client) throws IOException {
        OutputStream clientOutput = client.getOutputStream();
        String response = "HTTP/1.1 200 OK\r\nContent-Length:18\r\n\r\nEmpty Request?????";
        clientOutput.write(response.getBytes());
        clientOutput.flush();
        client.close();
    }

    public void giveFileOutput(String path, Socket client) throws IOException {
        File fileName = new File(path);
        try (BufferedReader fileReader = new BufferedReader(new FileReader(fileName))) {
            StringBuilder fileContent = new StringBuilder();
            String fileLine;
            while ((fileLine = fileReader.readLine()) != null) {
                fileContent.append(fileLine);
            }
            fileReader.close();
            String fileType = "";
            for (int i = 0; i < path.length(); i++) {
                if ((path.charAt(i) + "").equals(".")) {
                    fileType += path.substring(i + 1);
                }
            }

            // Prepare and send the HTTP response
            OutputStream clientOutput = client.getOutputStream();
            clientOutput.write("HTTP/1.1 200 OK\r\n".getBytes());
            String contentType = "Content-Type: text/" + fileType + "\r\n\r\n";
            clientOutput.write(contentType.getBytes());
            clientOutput.write("\r\n".getBytes());
            clientOutput.write(fileContent.toString().getBytes());
            clientOutput.flush();
        } catch (FileNotFoundException e) {
            throw e;
        } catch (IOException e) {
            System.out.println("Nah");
        }
    }

    public void checkFilesInDirectory(Socket client, String path) throws IOException {

        Main main = new Main();
        File directory = new File("/home/Javafiles");
        if (!directory.isDirectory()) {
            notFound(client);
        } else {
            File[] files = directory.listFiles();
            assert files != null;
            for (File file : files) {
                if (file.exists() && file.getName().equals(path)) {
                    main.giveFileOutput(path, client);
                } else {
                    main.notFound(client);
                }

            }
        }

    }

    public void notFound(Socket client) throws IOException {
        OutputStream clientOutput = client.getOutputStream();
        String response = "HTTP/1.1 404 ERROR\r\n Content-Length: 8\r\n\r\n 404 ERROR \n PAGE NOT FOUND!";
        clientOutput.write(response.getBytes());
        clientOutput.flush();
        client.close();
    }

    public static void main(String[] args) {
        Main main = new Main();
        // Start receiving messages
        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            // System.out.println("Server started.\n Listening for messages");
            while (true) {
                // Handle new incoming messages
                try (Socket client = serverSocket.accept()) {
                    // System.out.println("Debug: Got a new message "+ client.toString());

                    InputStreamReader input = new InputStreamReader(client.getInputStream());
                    BufferedReader buffer = new BufferedReader(input);
                    // System.out.println(buffer);
                    // Read the 1st Request from the client
                    StringBuilder request = new StringBuilder();
                    String line = buffer.readLine();
                    while (line != null && !line.isBlank()) {
                        request.append(line + "\r\n");
                        line = buffer.readLine();
                    }
                    System.out.println("----REQUEST----");
                    System.out.println(request);

                    String firstLine = request.toString().split("\n")[0];
                    // System.out.println(firstLine);
                    String resource = "";

                    for (int i = 5; i < firstLine.length(); i++) {
                        if ((firstLine.charAt(i) + "").equals(" ")) {
                            resource += firstLine.substring(5, i);
                            if (resource.contains(".jpg") || resource.contains(".jpeg") || resource.contains(".webp")) {
                                main.images(client, resource);
                            } else if (resource.contains(".html") || resource.contains(".css")
                                    || resource.contains(".txt")) {
                                main.giveFileOutput(resource, client);
                            }
                            break;
                        }

                    }
                    switch (resource) {
                        case "HelloWorld":
                            main.returnHelloWorld(client);
                            break;
                        case "Transition":
                            main.giveFileOutput(resource + "/Transition.html", client);
                            break;
                        case "":
                            main.noInput(client);
                            break;
                        default:
                            main.checkFilesInDirectory(client, resource);
                    }

                }

            }
        } catch (IOException exception) {
            System.out.println(exception.getMessage());

        }
    }
}
