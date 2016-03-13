models = ls('models');
models = models(3:end, :);
for ii = 1:size(models, 1)
    f = models(ii, :);
    [~, prefix, ~] = fileparts(f);
    command = sprintf('meshlabserver -i models\\%s -o models_off\\%s.off', f, prefix)
    system(command);
end