function config_swagger(url) {
    window.onload = function () {
        var ui = SwaggerUIBundle({
            url: url,
            dom_id: '#swagger-ui',
            deepLinking: true,
            displayOperationId: true,
            displayRequestDuration: true,
            presets: [
                SwaggerUIBundle.presets.apis
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ]
        });
        window.ui = ui
    };
}