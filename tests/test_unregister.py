from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_unregister_for_activity():
    email = "testuser2@mergington.edu"
    activity = "Programming Class"
    # Najpierw zapisz użytkownika
    client.post(f"/activities/{activity}/signup?email={email}")
    # Teraz wyrejestruj
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 200
    assert f"Removed {email} from {activity}" in response.json()["message"]
    # Próba ponownego wyrejestrowania powinna zwrócić 404
    response2 = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response2.status_code == 404
    assert response2.json()["detail"] == "Participant not found"
