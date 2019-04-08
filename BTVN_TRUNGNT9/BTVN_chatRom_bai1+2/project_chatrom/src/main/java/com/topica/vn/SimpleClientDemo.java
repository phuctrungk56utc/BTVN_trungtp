package com.topica.vn;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Scanner;
@SuppressWarnings("unused")
public class SimpleClientDemo{
    public final static String SERVER_IP = "127.0.0.1";
    public final static int SERVER_PORT = 7;
	private static final String SERVEeR_IP = null;
 
    public static void main(String[] args) throws IOException, InterruptedException {
        Socket socket = null;
        try {
            socket = new Socket(SERVEeR_IP, SERVER_PORT); // Connect to server
            System.out.println("Connected: " + socket);

            Scanner input = new Scanner(System.in);
            DataInputStream iOS = new DataInputStream(socket.getInputStream());
            DataOutputStream dOS = new DataOutputStream(socket.getOutputStream());
            while(true) {
            	System.out.println("Nhập vào 1 cai gi   : ");
            	String string = input.nextLine();
            	//sc.nextInt();
            	dOS.writeUTF(string);
            	String ch = iOS.readUTF();
            	System.out.print(ch + " " + "\n"); 
                Thread.sleep(200);
            }
        } catch (IOException ie) {
            System.out.println("Can't connect to server");
        } finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}