using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using System.Text;
using System.IO;

public class UnityApp : MonoBehaviour
{
    private string flaskUrl = "http://localhost:5000";

    void Start()
    {
        // Exemplo de manipulação de lista: enviar lista de números para somar
        StartCoroutine(SendListToFlask());

        // Exemplo de upload de arquivo
        StartCoroutine(UploadFileToFlask("path_to_your_file.txt"));

        // Exemplo de leitura de arquivo
        StartCoroutine(ReadFileFromFlask("file_uploaded.txt"));
    }

    IEnumerator SendListToFlask()
    {
        string jsonData = "{\"numbers\":[1, 2, 3, 4, 5]}";
        byte[] bodyRaw = Encoding.UTF8.GetBytes(jsonData);
        var request = new UnityWebRequest(flaskUrl + "/sum-list", "POST");
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError(request.error);
        }
        else
        {
            Debug.Log("Sum result: " + request.downloadHandler.text);
        }
    }

    IEnumerator UploadFileToFlask(string filePath)
    {
        byte[] fileData = File.ReadAllBytes(filePath);
        WWWForm form = new WWWForm();
        form.AddBinaryData("file", fileData, Path.GetFileName(filePath), "text/plain");

        UnityWebRequest request = UnityWebRequest.Post(flaskUrl + "/upload-file", form);

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError(request.error);
        }
        else
        {
            Debug.Log("File upload result: " + request.downloadHandler.text);
        }
    }

    IEnumerator ReadFileFromFlask(string filename)
    {
        string jsonData = "{\"filename\":\"" + filename + "\"}";
        byte[] bodyRaw = Encoding.UTF8.GetBytes(jsonData);
        var request = new UnityWebRequest(flaskUrl + "/read-file", "POST");
        request.uploadHandler = new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError(request.error);
        }
        else
        {
            Debug.Log("File content: " + request.downloadHandler.text);
        }
    }
}
