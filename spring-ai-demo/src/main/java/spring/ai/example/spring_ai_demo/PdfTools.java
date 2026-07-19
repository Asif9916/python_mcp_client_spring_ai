package spring.ai.example.spring_ai_demo;

import org.springaicommunity.mcp.annotation.McpTool;
import org.springaicommunity.mcp.annotation.McpToolParam;
import org.springframework.stereotype.Component;
import spring.ai.example.spring_ai_demo.PdfService;

@Component
public class PdfTools {

    private final PdfService pdfService;

    public PdfTools(PdfService pdfService) {
        this.pdfService = pdfService;
    }

    @McpTool(name = "askPdf", description = "Answer questions from the loaded PDF")
    public String askPdf(
            @McpToolParam(description = "Question") String question) {

        return pdfService.ask(question);
    }
}
