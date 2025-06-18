# Frequently Asked Questions (FAQ)

This document answers common questions about the Renesis AI Assistant.

## General Questions

### What is the Renesis AI Assistant?

The Renesis AI Assistant is an AI-powered Slack bot designed to provide intelligent responses and assistance. It uses advanced natural language processing (GPT-4o) and vector search technology (Pinecone) to provide accurate, contextual answers with source references.

### What content does the bot have access to?

Currently, the bot has access to:
- Week 1 coaching call transcripts
- Week 1 PDF materials and guides
- Program protocols and procedures for Week 1
- Troubleshooting guides and FAQs for Week 1

**Note**: The bot is limited to Week 1 content only in this MVP version.

### How accurate are the bot's responses?

The bot aims for 80-90% accuracy on common Week 1 questions. Accuracy depends on:
- Quality of the source content
- Clarity of the user's question
- Availability of relevant information in the knowledge base

### Can the bot provide medical advice?

**No.** The bot provides educational information based on program content but cannot:
- Diagnose medical conditions
- Provide personalized medical advice
- Replace consultation with healthcare professionals
- Make treatment recommendations

Always consult with qualified healthcare providers for medical concerns.

## Usage Questions

### How do I ask the bot a question?

There are several ways to interact with the bot:

1. **In channels**: Mention the bot with your question
   ```
   @gutless-assistant What foods should I avoid in Week 1?
   ```

2. **Direct messages**: Send a direct message to the bot
   ```
   Can you explain the elimination protocol?
   ```

3. **Thread replies**: The bot can continue conversations in threads

### What types of questions can I ask?

You can ask about:
- **Protocols**: "What's the Week 1 morning routine?"
- **Foods**: "What can I eat during the elimination phase?"
- **Symptoms**: "What symptoms are normal in Week 1?"
- **Procedures**: "How do I prepare for Week 1?"
- **Troubleshooting**: "I'm having issues with [specific problem]"
- **Clarifications**: "Can you explain [specific concept] better?"

### Why doesn't the bot understand my question?

Common reasons include:
- **Too vague**: "Help me" vs. "What foods should I avoid in Week 1?"
- **Outside scope**: Questions about Week 2+ content
- **Unclear phrasing**: Try rephrasing more specifically
- **Missing context**: Include relevant details

### How long does it take to get a response?

- **Typical response time**: 2-5 seconds
- **Complex questions**: 5-10 seconds
- **High load periods**: Up to 30 seconds

If no response after 30 seconds, try asking again.

### Can I ask follow-up questions?

Yes! The bot can handle follow-up questions in the same conversation thread. For example:

```
User: What foods are eliminated in Week 1?
Bot: [Lists eliminated foods]
User: Why are these foods eliminated?
Bot: [Explains the reasoning]
```

## Technical Questions

### What technology powers the bot?

The bot uses:
- **AI Model**: OpenAI GPT-4o for answer generation
- **Embeddings**: OpenAI text-embedding-ada-002 for semantic search
- **Vector Database**: Pinecone for content storage and retrieval
- **Platform**: Slack Bolt SDK for Python
- **Transcription**: OpenAI Whisper for audio processing

### How does the bot find relevant information?

The process involves:
1. **Query embedding**: Your question is converted to a vector
2. **Similarity search**: The vector database finds similar content
3. **Context assembly**: Relevant chunks are combined
4. **Answer generation**: GPT-4o creates an answer using the context
5. **Source linking**: References are added to the response

### Is my data private and secure?

**Privacy measures**:
- Questions and responses are logged for improvement purposes only
- No personal health data is stored beyond what you share in questions
- All API communications use HTTPS encryption
- Data is handled according to privacy best practices

**What's stored**:
- Your questions and bot responses (for analytics)
- Slack user IDs (for logging purposes)

**What's NOT stored**:
- Private Slack conversations outside bot interactions
- Personal files or attachments
- Sensitive personal information

### Can I use the bot offline?

No, the bot requires internet connectivity to:
- Access OpenAI APIs
- Query the Pinecone vector database
- Communicate with Slack

## Content and Accuracy Questions

### What if the bot gives incorrect information?

If you notice incorrect information:
1. **Cross-reference** with original program materials
2. **Report the issue** with specific details
3. **Ask for clarification** or rephrase your question
4. **Consult program coaches** for verification

### How often is the content updated?

Currently, the bot contains Week 1 content that was ingested during setup. Content updates require:
- Manual re-ingestion of new materials
- System administrator intervention
- Potential downtime during updates

### Can the bot access new Week 1 materials?

Not automatically. New materials must be:
- Processed through the content ingestion pipeline
- Converted to embeddings
- Added to the vector database

This requires technical intervention.

### Why does the bot sometimes say "I don't know"?

This happens when:
- The question is outside the Week 1 scope
- No relevant content is found in the database
- The confidence score is too low
- The question is too ambiguous

## Troubleshooting Questions

### The bot isn't responding. What should I do?

1. **Check bot status**: Is it showing as online in Slack?
2. **Try rephrasing**: Make your question more specific
3. **Wait and retry**: There might be temporary issues
4. **Check spelling**: Ensure you're mentioning the correct bot name
5. **Try direct message**: Sometimes channel mentions fail

### The bot gave an error message. What does it mean?

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "I'm having trouble processing your request" | General system error | Try again in a few minutes |
| "No relevant content found" | No matching information | Rephrase or ask about Week 1 topics |
| "Service temporarily unavailable" | API issues | Wait and retry |
| "I can only answer questions about Week 1" | Out of scope | Ask about Week 1 content only |

### The response seems incomplete or cut off. Why?

This can happen due to:
- **Token limits**: Very long responses may be truncated
- **Network issues**: Connection problems during response
- **Rate limiting**: API limits reached

**Solution**: Ask for specific parts of the information you need.

### Can I get more detailed information?

Yes! Try:
- **Ask for elaboration**: "Can you explain that in more detail?"
- **Request specific aspects**: "What are the specific steps for [process]?"
- **Ask for examples**: "Can you give me examples of [concept]?"
- **Request sources**: "Where in the video is this discussed?"

## Administrative Questions

### Who can use the bot?

Access is typically limited to:
- Members of the designated Slack workspace
- Gutless program participants
- Authorized coaches and staff

### Can I add the bot to other channels?

This depends on:
- Bot permissions in your workspace
- Channel privacy settings
- Administrator policies

Try `/invite @gutless-assistant` in the desired channel.

### How do I report bugs or suggest improvements?

To report issues:
1. **Document the problem**: What happened vs. what you expected
2. **Include context**: Your exact question and the bot's response
3. **Note timing**: When did the issue occur
4. **Contact administrators**: Through designated support channels

### Can the bot be customized for our specific needs?

Potential customizations include:
- **Content scope**: Adding more weeks or programs
- **Response style**: Adjusting tone or format
- **Integration**: Connecting to other systems
- **Features**: Adding new capabilities

Customizations require development work and should be discussed with the technical team.

## Performance Questions

### Why are responses sometimes slow?

Response time can be affected by:
- **Question complexity**: More complex queries take longer
- **API load**: High usage of OpenAI or Pinecone services
- **Network conditions**: Internet connectivity issues
- **System load**: Multiple concurrent users

### Can I make the bot respond faster?

**Tips for faster responses**:
- Ask specific, focused questions
- Avoid very long or complex queries
- Use clear, simple language
- Ask one question at a time

### Does the bot work better at certain times?

Performance is generally consistent, but may be slower during:
- Peak usage hours
- API maintenance windows
- High network traffic periods

## Future Development Questions

### Will the bot support more content in the future?

Potential future enhancements:
- **Week 2+ content**: Expanding beyond Week 1
- **Multiple programs**: Supporting other coaching programs
- **Interactive features**: More sophisticated interactions
- **Integrations**: Connecting to other tools and platforms

### Can the bot learn from interactions?

Currently, the bot:
- **Logs interactions** for analysis
- **Does not learn automatically** from conversations
- **Requires manual updates** to improve responses

Future versions might include:
- Automatic learning capabilities
- Feedback-based improvements
- Adaptive response generation

### How can I stay updated on new features?

Stay informed through:
- Slack announcements in your workspace
- Program communication channels
- Documentation updates
- Release notes and changelogs

## Getting More Help

### Where can I find more detailed documentation?

- [Installation Guide](installation.md)
- [Usage Guide](usage.md)
- [Troubleshooting Guide](troubleshooting.md)
- [API Reference](api-reference.md)
- [Architecture Overview](architecture.md)

### Who should I contact for support?

**For usage questions**: Ask in your Slack workspace or consult this FAQ

**For technical issues**: Contact your system administrator or technical support team

**For content questions**: Consult with program coaches or refer to original materials

**For feature requests**: Submit through designated feedback channels

### Is there a user community or forum?

Check with your program administrators about:
- Dedicated Slack channels for bot discussions
- User feedback groups
- Community forums or resources
- Regular Q&A sessions

---

*This FAQ is regularly updated. If you have questions not covered here, please reach out through appropriate support channels.*