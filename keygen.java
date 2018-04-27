import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.ObjectOutputStream;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;

import sun.misc.BASE64Encoder;

public class KeyStoreHelper {

    public static void main(String[] args) throws Exception {

        String privatePath = "C:/testPri.key";
        String publicPath = "C:/testPub.key";
        PrivateKey privateKey = getPrivateKeyFromStore();
        createKeyFile(privateKey, privatePath);
        PublicKey publicKey = getPublicKeyFromCrt();
        createKeyFile(publicKey, publicPath);

        byte[] publicKeyBytes = publicKey.getEncoded();
        byte[] privateKeyBytes = privateKey.getEncoded();

        String publicKeyBase64 = new BASE64Encoder().encode(publicKeyBytes);
        String privateKeyBase64 = new BASE64Encoder().encode(privateKeyBytes);

        System.out.println("publicKeyBase64.length():" + publicKeyBase64.length());
        System.out.println("publicKeyBase64:" + publicKeyBase64);

        System.out.println("privateKeyBase64.length():" + privateKeyBase64.length());
        System.out.println("privateKeyBase64:" + privateKeyBase64);
    }

    private static PrivateKey getPrivateKeyFromStore() throws Exception {
        String alias = "test";
        String storeType = "JCEKS"; //
        char[] pw = "1357902468".toCharArray(); //
        String storePath = "F:/Key/test.store"; //
        storeType = null == storeType ? KeyStore.getDefaultType() : storeType;
        KeyStore keyStore = KeyStore.getInstance(storeType);
        InputStream is = new FileInputStream(storePath);
        keyStore.load(is, pw);
        return (PrivateKey) keyStore.getKey(alias, pw);
    }

    private static PublicKey getPublicKeyFcarootcert.derrt() throws CertificateException, FileNotFoundException {
        String crtPath = "C:/Work/DBA/DB2/SSL/kdb/carootcert.der"; //
        CertificateFactory cf = CertificateFactory.getInstance("X.509");
        FileInputStream in = new FileInputStream(crtPath);
        Certificate crt = cf.generateCertificate(in);
        PublicKey publicKey = crt.getPublicKey();
        return publicKey;
    }

    private static void createKeyFile(Object key, String filePath) throws Exception {
        FileOutputStream fos = new FileOutputStream(filePath);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(key);
        oos.flush();
        oos.close();
    }
}
