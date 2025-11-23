import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Card, Form, Button, Alert, Spinner, Badge } from 'react-bootstrap';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [modules, setModules] = useState([]);
  const [selectedModules, setSelectedModules] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  // Check API health on mount
  useEffect(() => {
    checkApiHealth();
    loadModules();
  }, []);

  const checkApiHealth = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/health`);
      if (response.data.status === 'healthy') {
        setApiStatus('connected');
      }
    } catch (err) {
      setApiStatus('disconnected');
      console.error('API health check failed:', err);
    }
  };

  const loadModules = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/modules`);
      setModules(response.data.modules || []);
    } catch (err) {
      console.error('Failed to load modules:', err);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!searchQuery.trim()) {
      setError('Lütfen bir arama terimi girin');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_URL}/api/search`, {
        query: searchQuery
      });
      
      setSearchResults(response.data.results || []);
      
      if (response.data.results.length === 0) {
        setError('Sonuç bulunamadı');
      }
    } catch (err) {
      setError('Arama sırasında bir hata oluştu: ' + err.message);
      console.error('Search error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleModuleToggle = (moduleId) => {
    setSelectedModules(prev => {
      if (prev.includes(moduleId)) {
        return prev.filter(id => id !== moduleId);
      } else {
        return [...prev, moduleId];
      }
    });
  };

  const handleAnalyze = async (verseId) => {
    if (selectedModules.length === 0) {
      setError('Lütfen en az bir modül seçin');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_URL}/api/analyze`, {
        verse_id: verseId,
        modules: selectedModules
      });
      
      alert('Analiz tamamlandı! Konsolu kontrol edin.');
      console.log('Analysis results:', response.data);
    } catch (err) {
      setError('Analiz sırasında bir hata oluştu: ' + err.message);
      console.error('Analysis error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ backgroundColor: '#f8f9fa', minHeight: '100vh', paddingTop: '2rem', paddingBottom: '2rem' }}>
      <Container>
        {/* Header */}
        <Row className="mb-4">
          <Col>
            <h1 className="text-center mb-3">
              <span style={{ color: '#0066cc' }}>ARISTO</span> Kuran Keşif Motoru
            </h1>
            <p className="text-center text-muted">
              Kuran ayetlerini aramak ve analiz etmek için gelişmiş keşif platformu
            </p>
            <div className="text-center">
              <Badge bg={apiStatus === 'connected' ? 'success' : apiStatus === 'disconnected' ? 'danger' : 'warning'}>
                API: {apiStatus === 'connected' ? 'Bağlı' : apiStatus === 'disconnected' ? 'Bağlantı Yok' : 'Kontrol Ediliyor'}
              </Badge>
            </div>
          </Col>
        </Row>

        {/* Search Form */}
        <Row className="mb-4">
          <Col md={{ span: 8, offset: 2 }}>
            <Card>
              <Card.Body>
                <Form onSubmit={handleSearch}>
                  <Form.Group className="mb-3">
                    <Form.Label>Arama</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="Ayet metni, kavram veya kelime girin..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      disabled={loading}
                    />
                    <Form.Text className="text-muted">
                      Türkçe veya Arapça metin kullanabilirsiniz
                    </Form.Text>
                  </Form.Group>
                  <Button 
                    variant="primary" 
                    type="submit" 
                    disabled={loading}
                    className="w-100"
                  >
                    {loading ? (
                      <>
                        <Spinner animation="border" size="sm" className="me-2" />
                        Aranıyor...
                      </>
                    ) : (
                      'Ara'
                    )}
                  </Button>
                </Form>
              </Card.Body>
            </Card>
          </Col>
        </Row>

        {/* Modules Selection */}
        {modules.length > 0 && (
          <Row className="mb-4">
            <Col md={{ span: 8, offset: 2 }}>
              <Card>
                <Card.Body>
                  <h5 className="mb-3">Analiz Modülleri</h5>
                  <Row>
                    {modules.map(module => (
                      <Col md={6} key={module.id} className="mb-2">
                        <Form.Check
                          type="checkbox"
                          id={`module-${module.id}`}
                          label={`${module.name} - ${module.description}`}
                          checked={selectedModules.includes(module.id)}
                          onChange={() => handleModuleToggle(module.id)}
                        />
                      </Col>
                    ))}
                  </Row>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        )}

        {/* Error Alert */}
        {error && (
          <Row className="mb-4">
            <Col md={{ span: 8, offset: 2 }}>
              <Alert variant="danger" onClose={() => setError(null)} dismissible>
                {error}
              </Alert>
            </Col>
          </Row>
        )}

        {/* Search Results */}
        {searchResults.length > 0 && (
          <Row>
            <Col md={{ span: 8, offset: 2 }}>
              <h4 className="mb-3">Arama Sonuçları ({searchResults.length})</h4>
              {searchResults.map((result, index) => (
                <Card key={index} className="mb-3">
                  <Card.Body>
                    <Card.Title>
                      <Badge bg="info" className="me-2">{result.id}</Badge>
                      Sure {result.surah}, Ayet {result.verse}
                    </Card.Title>
                    <Card.Text className="mb-2" style={{ fontSize: '1.2rem', fontFamily: 'Arial', direction: 'rtl', textAlign: 'right' }}>
                      {result.arabic}
                    </Card.Text>
                    <Card.Text className="text-muted">
                      {result.translation}
                    </Card.Text>
                    <Button 
                      variant="outline-primary" 
                      size="sm"
                      onClick={() => handleAnalyze(result.id)}
                      disabled={loading || selectedModules.length === 0}
                    >
                      Analiz Et
                    </Button>
                    {selectedModules.length === 0 && (
                      <Form.Text className="text-muted ms-2">
                        Analiz için modül seçin
                      </Form.Text>
                    )}
                  </Card.Body>
                </Card>
              ))}
            </Col>
          </Row>
        )}

        {/* Welcome Message */}
        {searchResults.length === 0 && !error && !loading && (
          <Row>
            <Col md={{ span: 8, offset: 2 }}>
              <Card className="text-center">
                <Card.Body>
                  <h5>Aramaya Başlayın</h5>
                  <p className="text-muted">
                    Kuran ayetlerini aramak için yukarıdaki arama kutusunu kullanın.
                    Türkçe çeviri veya Arapça metin ile arama yapabilirsiniz.
                  </p>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        )}
      </Container>
    </div>
  );
}

export default App;
