In ambito di sicurezza applicativa, una vulnerabilità di **Remote Code Execution (RCE)** si verifica quando un'applicazione consente l'esecuzione di comandi o codice arbitrario da parte di un utente non autenticato o non autorizzato attraverso la rete.

In Python, le cause più comuni di RCE derivano dall'uso improprio di funzioni built-in come `eval()`, `exec()`, dall'esecuzione insicura di comandi di sistema tramite `os.system()` o `subprocess`, oppure dalla deserializzazione non sicura con moduli come `pickle`.

Di seguito viene illustrato un esempio basato su un'API vulnerabile che utilizza `eval()`, seguito dall'analisi dell'attacco e dalla relativa mitigazione.

---

### Scenario: Calcolatrice remota vulnerabile

Immaginiamo un semplice servizio web basato su **Flask** che accetta un'espressionematematica dall'utente e restituisce il risultato:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    # Recupera l'espressione dal parametro GET 'expr'
    user_expr = request.args.get('expr', '')
    
    # VULNERABILITÀ: 'eval' valuta arbitrariamente qualsiasi codice Python valido
    try:
        result = eval(user_expr)
        return f"Risultato: {result}"
    except Exception as e:
        return f"Errore: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Meccanismo di sfruttamento (Exploitation)

L'attaccante può sfruttare il fatto che `eval()` non si limita a calcoli matematici, ma può importare ed eseguire moduli Python tramite la built-in function `__import__()`.

#### 1. Richiesta lecita
```http
GET /calculate?expr=10*5 HTTP/1.1
Host: target:5000
```
*Output:* `Risultato: 50`

#### 2. Payload di esecuzione codice
Un attaccante invia un'espressione che invoca il modulo `os` o `subprocess` per eseguire comandi a livello di sistema operativo:

```http
GET /calculate?expr=__import__('os').popen('id').read() HTTP/1.1
Host: target:50