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

public class Main5 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			TextField tfMine   = (TextField) scene.lookup("#tfMine");
			TextField tfCom	   = (TextField) scene.lookup("#tfCom");
			TextField tfResult = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					
					String mine = tfMine.getText();
					
					int ran = (int)(Math.random() * 10) + 1;
					String com = null;
					if(ran % 2 == 0) {
						com = "Â¦";
					} else if(ran % 2 == 1) {
						com = "È¦";
					}
					
					tfCom.setText(com);
					
					if(mine.equals(com)) {
						tfResult.setText(ran + " Á¤´ä");
					} else {
						tfResult.setText(ran + " Æ²¸²");
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
