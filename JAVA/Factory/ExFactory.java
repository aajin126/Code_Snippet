package hj231207;

public class ExFactory {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Shared s = new Shared();
		FileRead file = new FileRead(s);
		Thread Seoul = new Thread(new SeoulFactory(s));
		Thread DaeGu = new Thread(new DaeGuFactory(s));
		Thread KwangJu = new Thread(new KwangJuFactory(s));
		Thread PuSan = new Thread(new PuSanFactory(s));
		
		file.setPriority(10);
        System.out.println("FileReader의 우선순위: " + file.getPriority());	
        Seoul.setPriority(7);
        System.out.println("서울의 우선순위: " + Seoul.getPriority());		
        DaeGu.setPriority(3);
        System.out.println("대구의 우선순위: " + DaeGu.getPriority());
        KwangJu.setPriority(3);
        System.out.println("광주의 우선순위: " + KwangJu.getPriority());
        PuSan.setPriority(3);
        System.out.println("부산의 우선순위: " + PuSan.getPriority());
		
		Seoul.start();
		DaeGu.start();
		KwangJu.start();
		PuSan.start();
		file.start();
	}

}
