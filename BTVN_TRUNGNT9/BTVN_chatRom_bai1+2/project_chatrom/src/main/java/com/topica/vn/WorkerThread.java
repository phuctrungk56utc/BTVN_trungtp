package com.topica.vn;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
 
public class WorkerThread extends Thread {
    private Socket socket;

    public WorkerThread(Socket socket) {
        this.socket = socket;
    }
    public void send(String message) throws IOException {
    	DataInputStream iOS = new DataInputStream(socket.getInputStream());
        DataOutputStream dOS = new DataOutputStream(socket.getOutputStream());
        dOS.writeUTF(message);
	}
    public void run() {
    	String sv;
    	DataInputStream iOS;
		try {
			iOS = new DataInputStream(socket.getInputStream());
			while (true) {
				String sv2 = iOS.readUTF();
				if (sv2 == "out")
					break;
				String message = new String(sv2);
				System.out.println(sv2);
				
			}
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        try {
			DataOutputStream dOS = new DataOutputStream(socket.getOutputStream());
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
    }
}