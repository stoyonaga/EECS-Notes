package com.example.project4443_prototype;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ProgressBar;
import android.widget.Spinner;

public class MainActivity extends AppCompatActivity {
    /**
     * Project4443 (Team Delta)
     * Author(s):
     * - Shogo Toyonaga
     * - Duaa Ali
     * - Mohammad Khan
     * - Seadric Macawile
     *
     * LOG:
     * 2023-02-02: Prototype now has core functionalities described in our topic
     * 2023-02-02: Documentation regarding MainActivity, ResultsActivity, and TypingActivity added
     * 2023-02-02: Dependencies have been added to Gradle and AndroidManifest
     * 2023-02-07: Bug Fixes with Levenshtein Distance
     * 2023-02-12: Added more strings for short/informal and long/formal text prompts
     * 2023-02-12: Fixed a bug where keyboard would take up the whole screen in landscape orientation (TypingActivity)
     * 2023-02-13: Fixed bug with keyboard input method in TypingActivity.java
     * 2023-02-14: Refactored LevenshteinDistance method into a separate class for JUnit Testing
     * 2023-02-14: Added Espresso UI Testing
     * 2023-03-04: Implemented onSaveInstanceState() and onRestoreInstanceState() to fix bugs with the text prompt in landscape mode.
     * 2023-03-04: Implemented landscape xml versions of each layout (res/layout-land/*.xml)
     * 2023-03-04: Found and fixed a bug with wpm calculation; we were not saving and restoring the start_time which led to wrong calculations.
     * 2023-03-04: Added Documentation
     * 2023-03-04: Adjusted UI to include padding
     * 2023-03-12: QOL Improvements: Adding features to EditText to start the timer when tapped
     * 2023-03-14: Final additions to the Macrobenchmark
     * 2023-03-22: Cleanup / Wrap-up
     *
     * Functional Hierarchy
     * MainActivity --> TypingActivity --> ResultsActivity --
     * ^                                                    |
     * |                                                    |
     * |                                                    |
     * |--------------------------------------------------- |
     *
     * Dependencies:
     * 1) org.apache.commons:commons-text:1.9 has been added to analyze text similarity via
     *    Levenshtein Distance
     * 2) android.os.Bundle
     * 3) java.uti.Random
     * 4) res > strings.xml contains two string-arrays which contain our prompts depending on the difficulty level.
     *
     * TODO:
     * 1) Add more prompts to simple_phrases and long_formal string-arrays [DONE]
     * 2) Implement handlers for Orientation changing [DONE]
     * 3) Unit Testing [DONE]
     * 4) Make UI Adjustments (Colour themes, View placements, etc.,)
     * 5) Macrobenchmarking Implementation for Bonus Marks
     * 6) Android Profiling
     * --------------------------------------------------------------------------
     */

    // ---------- Important Variables ----------

    // 1) State Settings for the TypingActivity
    Spinner inputType;
    Spinner levelType;
    ProgressBar page;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initialize();
    }

    /**
     * Once the user clicks the "Start" button, we will save the state of the app settings in an intent
     * and proceed to launch the Typing Activity.
     * @param view: The Button we will use to activate the onClickListener
     */
    public void onClick(View view){
        Intent i = new Intent(this, TypingActivity.class);
        i.putExtra("inputType", inputType.getSelectedItem().toString());
        i.putExtra("levelType", levelType.getSelectedItem().toString());
        startActivity(i);
    }

    /**
     * Initializes the variables which are declared above..
     */
    public void initialize(){
        inputType = findViewById(R.id.spinner_input);
        levelType = findViewById(R.id.spinner_level);
        page = findViewById(R.id.process_bar);
        page.setProgress(33, true);
    }
}