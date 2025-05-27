# Projeto WEB com FastAPI

### Servidores de aplicação python
 
Python web applications require a server to handle incoming HTTP requests and route them to the application code. WSGI and ASGI are specifications that define how web servers communicate with Python web applications or frameworks.

#### WSGI
- **WSGI (Web Server Gateway Interface):** A standard interface between web servers and Python web applications or frameworks for synchronous programming.
- `WSGI`: `Web Server Gateway Interface`

1. Especificação antiga
2. Projetada para aplicações síncronas
    > Processa as requisições uma por vez por um worker/thread. *Para lidar com múltiplas conexões simultâneas, os servidores WSGI geralmente usam múltiplos processos ou threads.*

#### ASGI
- **ASGI (Asynchronous Server Gateway Interface):** A spiritual successor to WSGI, it provides a standard interface between async-capable Python web servers, frameworks, and applications. It's designed to handle a large number of concurrent connections and supports protocols like WebSockets. FastAPI is an ASGI framework.
    - *Exemplos de servidores ASGI:* Uvicorn, Daphne, Hypercorn.
- `ASGI`: `Asynchronous Server Gateway Interface`

1. Evolução do `WSGI`
2. Projetada para aplicações assíncronas.
    - **Assíncrono**: Permite o uso de `async` e `await` do Python para operações não bloqueantes.
    - **Suporte a protocolos além do HTTP**: Pode lidar com `WebSockets`, `HTTP/2` e outros protocolos de longa duração.
    - **Flexibilidade**: Permite que uma única aplicação lide com diferentes tipos de eventos e protocolos.

---

- Ver IP no `Ubuntu | Linux`

```bash
$ ip addr
```
