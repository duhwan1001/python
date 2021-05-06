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
						com = "가위";
					} else if (ran == 2) {
						com = "바위";
					} else if (ran == 3) {
						com = "보";
					}

					tfCom.setText(com);

					if (mine.equals(com)) {
						tfResult.setText("비김");
					}

					if (mine.equals("가위") && com.equals("바위")) {
						tfResult.setText("패배");
					} else if (mine.equals("가위") && com.equals("보")) {
						tfResult.setText("이김");
					}
					if (mine.equals("바위") && com.equals("가위")) {
						tfResult.setText("이김");
					} else if (mine.equals("바위") && com.equals("보")) {
						tfResult.setText("패배");
					}
					if (mine.equals("보") && com.equals("가위")) {
						tfResult.setText("패배");
					} else if (mine.equals("보") && com.equals("바위")) {
						tfResult.setText("이김");
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
