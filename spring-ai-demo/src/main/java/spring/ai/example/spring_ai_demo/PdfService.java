package spring.ai.example.spring_ai_demo;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.document.Document;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.stereotype.Service;

@Service
public class PdfService {

        private final ChatClient chatClient;
        private final VectorStore vectorStore;

        public PdfService(ChatClient.Builder builder,
                        VectorStore vectorStore) {

                this.chatClient = builder.build();
                this.vectorStore = vectorStore;
        }

        public String ask(String question) {

                List<Document> docs = vectorStore.similaritySearch(question);

                String context = docs.stream()
                                .map(Document::getText)
                                .collect(Collectors.joining("\n"));

                return chatClient.prompt()

                                .system("""
                                                Answer ONLY from the supplied context.
                                                If the answer is not present,
                                                respond with:
                                                I don't know.
                                                """)

                                .user("""
                                                Context:

                                                %s

                                                Question:

                                                %s
                                                """.formatted(context, question))

                                .call()
                                .content();
        }
}
