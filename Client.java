package WebServerTrial;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        try {
            Socket connect = new Socket("localhost",6969);
            String output = System.getProperty("os.name")+", "+ connect.getInetAddress()+", "+System.getProperty("os.version")+", "+System.getProperty("user.name");
            BufferedOutputStream bos = new BufferedOutputStream(connect.getOutputStream());
            bos.write(output.getBytes());
            bos.flush();
            bos.close();
            connect.close();                

        } catch (IOException e) {

            System.out.println(e.getLocalizedMessage());
        }
    }
}
