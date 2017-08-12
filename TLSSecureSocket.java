//TLSSecureSocket.java
// Mod: Gisaza (2011)
// Remember in console -> # keytool -genkey -v -keyalg RSA -alias CertHost -keystore sslKeyStore
// sslKeyStore Repositorio de Certs, creado en directorio . (remember PATH)
// RUN java -Djavax.net.ssl.keyStore=sslKeyStore -Djavax.net.ssl.keyStorePassword=password TLSSecureSocket
import java.io.*;
import java.net.*;
import javax.net.ssl.*;
//
// TLS Server Socket
// 
public class TLSSecureSocket {
	public static void main(String[] args) throws IOException {
	//
	// Crear un socket seguro TLS/SSL vinculado al puerto 8080 
	SSLServerSocketFactory sslsf = (SSLServerSocketFactory)SSLServerSocketFactory.getDefault();
	ServerSocket ss = sslsf.createServerSocket(8080);
	// loop para esperar el connect
	while (true) {
		try {
			Socket s = ss.accept();
			System.out.println( "Conexion Cliente lista !" );
		//	obtener el client request
			BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
			System.out.println(in.readLine());
		//
		// salida HTML 
			PrintWriter out = new PrintWriter( s.getOutputStream() );
			System.out.println("<HTML><HEAD><TITLE>Secure HTTPS Server Example</TITLE> " +"</HEAD><BODY><H1>Hello World!</H1></BODY></HTML> \n");
			//
			// Cerrar el socket 
			out.close();
			s.close();
			}
		catch (Exception e) {
			e.printStackTrace();
		}
	}
	}
}
