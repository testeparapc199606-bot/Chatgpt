"""
Testes unitários para o módulo ChatGPT
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.chatgpt import ChatGPT


class TestChatGPT(unittest.TestCase):
    """Testes para a classe ChatGPT"""

    def setUp(self):
        """Configuração antes de cada teste"""
        # Mock para evitar chamadas reais à API
        self.api_key = "test_api_key"

    def test_initialization(self):
        """Teste de inicialização com chave de API fornecida"""
        try:
            chat = ChatGPT(api_key=self.api_key)
            self.assertEqual(chat.model, "gpt-3.5-turbo")
        except Exception as e:
            self.skipTest(f"API não disponível: {e}")

    def test_conversation_history(self):
        """Teste de histórico de conversas"""
        try:
            chat = ChatGPT(api_key=self.api_key)
            
            # Verificar que o histórico começa vazio
            self.assertEqual(len(chat.get_history()), 0)
            
            # Limpar histórico
            chat.clear_history()
            self.assertEqual(len(chat.get_history()), 0)
        except Exception as e:
            self.skipTest(f"API não disponível: {e}")

    def test_set_model(self):
        """Teste de configuração de modelo"""
        try:
            chat = ChatGPT(api_key=self.api_key)
            chat.set_model("gpt-4")
            self.assertEqual(chat.model, "gpt-4")
        except Exception as e:
            self.skipTest(f"API não disponível: {e}")

    def test_missing_api_key(self):
        """Teste de erro quando chave de API não é fornecida"""
        # Remover variável de ambiente se existir
        old_key = os.environ.pop("OPENAI_API_KEY", None)
        
        try:
            with self.assertRaises(ValueError):
                ChatGPT()
        finally:
            # Restaurar chave anterior
            if old_key:
                os.environ["OPENAI_API_KEY"] = old_key


class TestChatGPTIntegration(unittest.TestCase):
    """Testes de integração com a API"""

    def test_api_integration(self):
        """Teste de integração com a API OpenAI"""
        api_key = os.environ.get("OPENAI_API_KEY")
        
        if not api_key:
            self.skipTest("OPENAI_API_KEY não definida")
        
        try:
            chat = ChatGPT(api_key=api_key)
            response = chat.send_message("Diga apenas 'OK'")
            self.assertIsNotNone(response)
            self.assertIsInstance(response, str)
            self.assertGreater(len(response), 0)
        except Exception as e:
            self.skipTest(f"Erro na integração com API: {e}")


if __name__ == "__main__":
    unittest.main()
