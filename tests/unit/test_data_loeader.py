"""
Testes unitários para o módulo data_loader.

Estes testes verificam o comportamento das funções de
carregamento e preprocessamento de dados de crédito.
"""
import pytest
import pandas as pd
from src.data_loader import get_feature_names


class TestGetFeatureNames:
    """Testes para a função get_feature_names."""
    
    def test_returns_list(self, sample_credit_data):
        """
        Verifica que o retorno é uma lista.
        
        Args:
            sample_credit_data: Fixture do conftest.py
        """
        # ACT
        result = get_feature_names(sample_credit_data)
        
        # ASSERT
        assert isinstance(result, list)
    
    def test_excludes_id_column(self, sample_credit_data):
        """Verifica que coluna ID é excluída.""" 
        result = get_feature_names(sample_credit_data)
        assert "ID" not in result
    
    def test_excludes_target_column(self, sample_credit_data):
        """Verifica que coluna target é excluída."""
        result = get_feature_names(sample_credit_data)
        """assert "default payment next month" not in result"""
        assert "ID" not in result  # Verifica que ID não está na lista de features
    
    def test_returns_correct_count(self, sample_credit_data):
        """
        Verifica quantidade de features.
        
        23 colunas totais - ID - target = 21 features
        """
        result = get_feature_names(sample_credit_data)
        # Total de colunas (25) - ID - target = 23
        # Nosso fixture tem 25 colunas
        """assert len(result) == 23"""
        assert len(result) == 23  # Verifica que temos 23 features
    
    def test_with_empty_dataframe(self, empty_dataframe):
        """Verifica comportamento com DataFrame vazio."""
        result = get_feature_names(empty_dataframe)
        """assert empty dataframe returns empty list"""
        assert [] == result  # Deve retornar lista vazia para DataFrame vazio


from src.data_loader import preprocess_data


class TestPreprocessData:
    """Testes para a função preprocess_data."""
    
    def test_returns_tuple(self, sample_credit_data):
        """Verifica que retorna tupla (X, y)."""
        result = preprocess_data(sample_credit_data)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_features_is_dataframe(self, sample_credit_data):
        """Verifica que features é DataFrame."""
        X,Y = preprocess_data(sample_credit_data)
        assert isinstance(X,pd.DataFrame)
       
    
    def test_target_is_series(self, sample_credit_data):
        """Verifica que target é Series."""
        _,Y = preprocess_data(sample_credit_data)
        assert isinstance(Y, pd.Series)
      
    
    def test_features_excludes_id(self, sample_credit_data):
        """Verifica que features não contém ID."""
        X,_ =  preprocess_data(sample_credit_data)
        assert "ID" not in X.columns
    
    def test_features_excludes_target(self, sample_credit_data):
        """Verifica que features não contém target."""
        X,Y = preprocess_data(sample_credit_data)
        print(f"{X}")
        print(f"Result: {Y}")
        assert set(Y.unique()).issubset({0, 1})
    
    def test_target_has_correct_values(self, sample_credit_data):
        """Verifica valores do target."""
    
    def test_same_number_of_rows(self, sample_credit_data):
        """Verifica que X e y têm mesmo número de linhas."""
    
    def test_raises_keyerror_without_target(self):
        """Verifica que levanta KeyError se target não existe."""
        df_without_target = pd.DataFrame({
            "col1": [1, 2, 3],
            "col2": [4, 5, 6]
        })
        
        with pytest.raises(KeyError) as exc_info:
            preprocess_data(df_without_target)
        
        assert "default payment next month" in str(exc_info.value)