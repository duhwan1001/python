package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			TextField tfMine = (TextField) scene.lookup("#tfMine");
			TextField tfCom = (TextField) scene.lookup("#tfCom");
			TextField tfResult = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");

			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {

					String mine = tfMine.getText();

					int ran = (int) (Math.random() * 3) + 1;
					String com = null;
					if (ran == 1) {
						com = "����";
					} else if (ran == 2) {
						com = "����";
					} else if (ran == 3) {
						com = "��";
					}

					tfCom.setText(com);

					if (mine.equals(com)) {
						tfResult.setText("���");
					}

					if (mine.equals("����") && com.equals("����")) {
						tfResult.setText("�й�");
					} else if (mine.equals("����") && com.equals("��")) {
						tfResult.setText("�̱�");
					}
					if (mine.equals("����") && com.equals("����")) {
						tfResult.setText("�̱�");
					} else if (mine.equals("����") && com.equals("��")) {
						tfResult.setText("�й�");
					}
					if (mine.equals("��") && com.equals("����")) {
						tfResult.setText("�й�");
					} else if (mine.equals("��") && com.equals("����")) {
						tfResult.setText("�̱�");
					}

				}
			});

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
