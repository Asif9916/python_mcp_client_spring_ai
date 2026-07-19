package spring.ai.example.spring_ai_demo;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.document.Document;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import spring.ai.example.spring_ai_demo.PdfService;

@RestController
@RequestMapping("/chat")
public class MyController {

    private final PdfService pdfService;

    public MyController(PdfService pdfService) {
        this.pdfService = pdfService;
    }

    @GetMapping("/ask")
    public String ask(@RequestParam String question) {

        return pdfService.ask(question);

    }

}
