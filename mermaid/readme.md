```mermaid
sequenceDiagram
Wechaty->>QA_api: Question xxx
loop Questioncheck
    QA_api->>Opensearch: Question is exist or not    
end
QA_api-->>Wechaty: Answer

```

