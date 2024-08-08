package com.ntousoselab.karate;

import com.ntousoselab.karate.core.DataTablesHandler;
import com.ntousoselab.karate.core.OperationHandler;
import com.ntousoselab.karate.core.ParametersHandler;
import com.ntousoselab.karate.core.RequestDataHandler;
import com.ntousoselab.karate.generator.KarateFileGenerator;
import com.ntousoselab.karate.generator.KarateElementGenerator;
import com.ntousoselab.karate.tag.GherkinTag;

import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        GherkinTag gherkinTag = new GherkinTag();
        ParametersHandler parameters = new ParametersHandler();
        RequestDataHandler requestData = new RequestDataHandler();
        DataTablesHandler dataTables = new DataTablesHandler(requestData);
        OperationHandler operationHandler = new OperationHandler(gherkinTag, parameters, requestData, dataTables);
        KarateElementGenerator karateElementGenerator = new KarateElementGenerator(operationHandler);
        KarateFileGenerator karateFileGenerator = new KarateFileGenerator(karateElementGenerator);
        List<String> errors = new ArrayList<>();
        karateFileGenerator.convertGherkinToKarate(errors);
        if (!errors.isEmpty()) {
            System.out.println("Errors encountered:");
            errors.forEach(System.out::println);
        }
    }
}
