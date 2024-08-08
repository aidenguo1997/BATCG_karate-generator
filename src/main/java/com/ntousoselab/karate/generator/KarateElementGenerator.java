package com.ntousoselab.karate.generator;

import com.ntousoselab.karate.core.OperationHandler;
import io.swagger.v3.oas.models.OpenAPI;

import java.util.List;
import java.util.Map;

public class KarateElementGenerator {
    private final OperationHandler operationHandler;

    public KarateElementGenerator(OperationHandler operationHandler) {
        this.operationHandler = operationHandler;
    }

    public void backgroundKarateScript(OpenAPI openAPI, String gherkinContent, List<Map<String, String>> requestDataList, List<String> errors, StringBuilder karateScript) {
        operationHandler.handleOperation(openAPI, gherkinContent, requestDataList, true, karateScript, errors);
    }

    public void scenarioKarateScript(OpenAPI openAPI, String gherkinContent, List<Map<String, String>> requestDataList, List<String> errors, StringBuilder karateScript) {
        operationHandler.handleOperation(openAPI, gherkinContent, requestDataList, false, karateScript, errors);
    }
}
