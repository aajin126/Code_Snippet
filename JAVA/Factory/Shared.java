package hj231207;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Shared {
	private int[][] data = new int[4][4];
	
	public Shared() {
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++)
				data[i][j] = 0;
		}
	}
	
	public synchronized int[] getFactory(String factory) {
		boolean check = false;
		while(true){
			for(int i=0;i<4;i++) {
				for(int j=0;j<4;j++)
					if(data[i][j] != 0) check=true;
			}
			if(check) break;
			
			try {
				System.out.println(factory+": 아직 파일 읽기 전입니다. wait에 들어갑니다.");
				wait();
	
			} catch(InterruptedException e) {
				e.printStackTrace();
			}
		}
		
		switch(factory) {
		case "Seoul":
			return data[0];
		case "DaeGu":
			return data[1];
		case "KwangJu":
			return data[2];
		case "PuSan":
			return data[3];
		}
		return null;
	};
	
	public synchronized void read() {
		FileReader fin = null;
		System.out.println("FileRead 스레드 ==== car.csv 파일 read ====");
		
		try {
			fin = new FileReader("D:/이하진/이화여대/23-2/java/car.csv");
			BufferedReader buf = new BufferedReader(fin);
			
			String line;
			buf.readLine();
			for(int i=0;i<4;i++) {
				line = buf.readLine();
				System.out.println("FileRead 스레드 ==== "+line+" ====");
                String[] column = line.split(",");
                for(int j=0;j<4;j++) {
                	data[i][j] = Integer.parseInt(column[j+1]);
                }
			}
			
			
			for(int i=0;i<4;i++) {
				line = buf.readLine();
				System.out.println("FileRead 스레드 ==== "+line+" ====");
                String[] column = line.split(",");
                for(int j=0;j<4;j++) {
                	data[i][j] += Integer.parseInt(column[j+1]);
                }
			}
			fin.close();
			buf.close();
			notifyAll();
		}
		catch (IOException e) {
			System.out.println("입출력 오류");
		}
	}
}
