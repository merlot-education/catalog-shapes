FROM maven:3-eclipse-temurin-17-alpine AS build

ARG SERVICE_VERSION=1.0.1

COPY catalog-shapes/ /catalog-shapes/

RUN apk add --no-cache python3 py3-rdflib &&\
    cd /catalog-shapes &&\
    python3 merge_shapes.py

COPY gxfs-catalog/add_merlot_pubkey.patch /add_merlot_pubkey.patch
COPY gxfs-catalog/truncate_schemas.patch /truncate_schemas.patch
RUN apk add --no-cache git maven &&\
    git clone -b main https://gitlab.eclipse.org/eclipse/xfsc/cat/fc-service.git &&\
    cd /fc-service &&\
	git checkout $SERVICE_VERSION &&\
	git apply /add_merlot_pubkey.patch &&\
	git apply /truncate_schemas.patch &&\
    rm -rf fc-service-core/src/main/resources/defaultschema/ontology &&\
    rm fc-service-core/src/main/resources/defaultschema/shacl/mergedShapesGraph.ttl &&\
    cp /catalog-shapes/shacl/shapes/mergedShapes.ttl fc-service-core/src/main/resources/defaultschema/shacl/mergedShapesGraph.ttl &&\
    cp -r /catalog-shapes/shacl/ontology fc-service-core/src/main/resources/defaultschema/ontology &&\
    mvn clean package -pl fc-service-server -am -Dmaven.test.skip=true

FROM eclipse-temurin:17-jre-alpine
COPY --from=build /fc-service/fc-service-server/target/fc-service-server-*.jar /opt/fc-service-server.jar
ENTRYPOINT ["java", "-jar","/opt/fc-service-server.jar"]
